import course_finder
import pdfplumber
import re


# Compare with student transcript file
def transferCredit(course_id):
    for credit in course_credits:
        if int(course_id) == int(credit["course_id"]):
            print("Credit found: "+str(credit["course_id"])+" "+str(credit["course_name"]))
            return True
    return False


# Initialize variables
pdf = pdfplumber.open('degrees\\DP-Traditional.pdf')
transcript_path = 'transcripts\\roy-kent.pdf'
course_groups = {}
title = ''
text = ''
pattern = r"([A-Za-z\s&,]+)" \
              r"(CS|SE)\s" \
              r"(\d{4})"

# Find courses in transcript
course_credits = course_finder.get_courses(transcript_path)

# Extract the text from the degree
for page in pdf.pages:
    text += page.extract_text()

# Loop through each line and the line following it if available
lines = text.split('\n')
for i, line in enumerate(lines):
    line = line.strip()
    if i + 1 < len(lines):
        next_line = lines[i + 1].strip()

        # If next line is a course but not this line, we have a new course group
        if re.match(pattern, next_line):
            if not re.match(pattern, line):

                # Save the current line as a course group title
                title = line
                courses = []
                course_groups[title] = courses

    # Otherwise, if only this line is a course, add it to the current course group
    if re.match(pattern, line):
        course_line = re.findall(pattern, line)
        for course in course_line:

            # Course information will include whether a student can transfer the credit
            info = {
                "title": course[0],
                "department": course[1],
                "id": course[2],
                "credit": "transferred" if transferCredit(course[2]) else None
            }
            course_groups[title].append(info)

# Print the courses for each course group
for course_group, courses in course_groups.items():
    print("\n")
    print(course_group)
    for course in courses:
        print(course)
