import re
import pdfplumber


def get_courses(path_to_pdf):
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

    # Open the PDF file, and concatenate all text into one string keeping as much formatting as possible
    with pdfplumber.open(path_to_pdf) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

    # Find all semesters in the text
    sections = re.split(semester_pattern, text)

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

    # Print the list of courses
    for course in courses:
        print(course)
    print(len(courses))
