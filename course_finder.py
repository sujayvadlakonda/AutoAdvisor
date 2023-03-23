import re
import pdfplumber

# 0 Define variables
courses = []  # A list of dictionaries to store the course information
season, year = "", ""  # Empty strings to avoid nulls
semester_pattern = r"(\d{4}\s)(Summer|Spring|Fall|Winter)"  # A regex pattern to find course semesters using 2 chunks
course_pattern = r"([A-Z]{2,4}\s)" \
                 r"(\d{4}\s)" \
                 r"([A-Z\:\+\s\/&-]+\s)" \
                 r"(\d+.\d+\s)" \
                 r"(\d+.\d+\s)" \
                 r"([A-Z]{1,2}[+|-]?\s)?" \
                 r"(\d+.\d+)?"  # A regex pattern to find course information using 7 chunks


# 1 Open the PDF file, and concatenate all text into one string keeping as much formatting as possible
with pdfplumber.open('transcript.pdf') as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()


# 2 Split the text into a new section when a year-semester pattern is found
sections = re.split(semester_pattern, text)


# 3 Divide text sections into three parts and treat accordingly
for x, section in enumerate(sections):

    # 3.1 Save season for reference
    if x % 3 == 1:
        season = section

    # 3.2 Save year for reference
    elif x % 3 == 1:
        year = section

    # 3.3 Find all matches of the course pattern in the semester section
    else:
        found_courses = re.findall(course_pattern, section)

        # 3.4 Iterate over found courses and save the data in a course structure
        for found_course in found_courses:
            course = {
                "year": year,
                "season": season,
                "subject": found_course[0],  # ([A-Z]{2,4}\s)
                "course_id": found_course[1],  # (\d{4}\s)
                "course_name": found_course[2],  # ([A-Z\:\+\s\/&-]+\s)
                "attempted": float(found_course[3]),  # (\d+.\d+\s)
                "earned": float(found_course[4]),  # (\d+.\d+\s)
                "grade": found_course[5] if found_course[5] else None,  # ([A-Z]{1,2}[+|-]?\s)
                "points": float(found_course[6])  # (\d+.\d+)
            }

            # 3.5 Save the course
            courses.append(course)


# 4 Print the list of courses
for course in courses:
    print(course)
print(len(courses))
