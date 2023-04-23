import pdfplumber
import re


# https://stackoverflow.com/questions/199059/a-pythonic-way-to-insert-a-space-before-capital-letters
# Some pdfs don't split camel case. Mike Modano is an example
def _split_camel_case(text):
    return re.sub(r"(?<=\w)([A-Z])", r" \1", text)


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
        stu_id = match.group()
        stu_id = re.sub(r"Student ID: ", "", stu_id)
        return stu_id

    def get_major(self):
        section_title = r"^Program:.*Master"
        major = r".*Major"
        regex = section_title + r".*" + major

        match = re.search(regex, self.text, flags=re.MULTILINE | re.DOTALL)
        major = match.group()
        major = re.search(r"^.*Major.*$", major, flags=re.MULTILINE).group()
        major = re.sub(r".*: ", "", major).strip()
        major = _split_camel_case(major)

        return major

    def get_beginning_of_graduate_record(self):
        section_title_regex = r"^Beginning ?of ?Graduate ?Record"
        semester_regex = r"\d{4} ?(Summer|Spring|Fall|Winter)"
        regex = section_title_regex + r"\n" + semester_regex
        match = re.search(regex, self.text, flags=re.MULTILINE)
        semester = match.group()
        semester = re.sub("^.*\n", "", semester)
        semester = _split_camel_case(semester)
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
