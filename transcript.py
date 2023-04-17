import pdfplumber
import re


class Transcript:
    def __init__(self, path_to_pdf):
        self.text = ""

        with pdfplumber.open(path_to_pdf) as pdf:
            for page in pdf.pages:
                self.text += page.extract_text()

    def get_name(self):
        match = re.search(r"^Name.*$", self.text, flags=re.MULTILINE)
        name = match.group()
        name = re.sub(r"Name: ", "", name)
        return name

    def get_id(self):
        match = re.search(r"^Student ID.*$", self.text, flags=re.MULTILINE)
        id = match.group()
        id = re.sub(r"Student ID: ", "", id)
        return id

    def get_major(self):
        section_title = r"^Program:.*Master"
        major = r".*Major"
        regex = section_title + r".*" + major

        match = re.search(regex, self.text, flags=re.MULTILINE | re.DOTALL)
        major = match.group()
        major = re.search(r"^.*Major.*$", major, flags=re.MULTILINE).group()
        major = re.sub(r".*: ", "", major).strip()
        major = self._split_camel_case(major)

        return major

    def get_beginning_of_graduate_record(self):
        section_title_regex = r"^Beginning ?of ?Graduate ?Record"
        semester_regex = r"\d{4} ?(Summer|Spring|Fall|Winter)"
        regex = section_title_regex + r"\n" + semester_regex
        match = re.search(regex, self.text, flags=re.MULTILINE)
        semester = match.group()
        semester = re.sub("^.*\n", "", semester)
        semester = self._split_camel_case(semester)
        return semester

    def get_combined_cumulative_gpa(self):
        section_title_regex = r"^Graduate ?Career ?Totals"
        gpa_regex = r"Combined ?Cum ?GPA ?\d\.\d{3}"
        regex = section_title_regex + r".*" + gpa_regex
        match = re.search(regex, self.text, flags=re.MULTILINE | re.DOTALL)
        match = match.group()
        match = re.search(gpa_regex, match, flags=re.MULTILINE)
        match = match.group()
        gpa = re.sub(r"Combined ?Cum ?GPA ?", "", match)
        return gpa

    def get_courses(self):
        courses = []  # A list of dictionaries to store the course information

        season, year = "", ""  # Empty strings to avoid nulls
        semester_pattern = r"(\d{4}\s?)(Summer|Spring|Fall|Winter)"  # A regular expression pattern to find course semesters
        course_pattern = (
            r"([A-Z]{2,4}\s)"
            r"(\d{4}\s)"
            r"([A-Z\:\+\s\/&-]+\s)"
            r"(\d+.\d+\s)"
            r"(\d+.\d+\s)"
            r"([A-Z]{1,2}[+|-]?\s)?"
            r"(\d+.\d+)?"
        )  # A regular expression pattern to find course information

        # Find all semesters in the text
        sections = re.split(semester_pattern, self.text)

        # Divide sections into three parts and treat accordingly
        for x, section in enumerate(sections):
            if x % 3 == 2:
                season = section.strip()
            elif x % 3 == 1:
                year = section.strip()
            else:
                # Find all matches of the course pattern in the semester section
                found_courses = re.findall(course_pattern, section)
                # Iterate over the matches and add them to the list of courses
                for found_course in found_courses:
                    course = {
                        "year": year,
                        "season": season,
                        "subject": found_course[0],
                        "course_id": found_course[1],
                        "course_name": found_course[2],
                        "attempted": float(found_course[3]),
                        "earned": float(found_course[4]),
                        "grade": found_course[5] if found_course[5] else None,
                        "points": float(found_course[6]),
                    }
                    courses.append(course)

        return courses

    # https://stackoverflow.com/questions/199059/a-pythonic-way-to-insert-a-space-before-capital-letters
    # Some pdfs don't split camel case. Mike Modano is an example
    def _split_camel_case(self, text):
        return re.sub(r"(?<=\w)([A-Z])", r" \1", text)
