from transcript import Transcript
from requirement import SimpleRequirement, MultiRequirement
from course import Courses

transcript = Transcript("transcripts/ted-lasso.pdf")
courses = transcript.get_courses()
courses = Courses(courses)

# Prints a dictionary w/ course info
print(SimpleRequirement("CS 6313").is_met(courses))
print(SimpleRequirement("CS 6350").is_met(courses))
print(SimpleRequirement("CS 6363").is_met(courses))
print(SimpleRequirement("CS 6375").is_met(courses))
print(
    MultiRequirement(["CS 6301", "CS 6320", "CS 6327", "CS 6347", "CS 6360"]).is_met(
        courses
    )
)

# Print False
print(SimpleRequirement("CS LMAO").is_met(courses))
print(SimpleRequirement("CS ROFL").is_met(courses))
