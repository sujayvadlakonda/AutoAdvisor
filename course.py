class LevelingCourseStatus:
    COMPLETED = "Completed"
    WAIVED = "Waived"
    NOT_REQUIRED = "Not required by plan or elective"
    OTHER = "Other"


class LevelingCourse():
    def __init__(self, id, status=LevelingCourseStatus.COMPLETED):
        self.id = id
        self.status = status

    def to_string(self, courses):
        string = self.id + " " + self.status

        if self.status == LevelingCourseStatus.COMPLETED:
            course = courses_contains(courses, self.id)
            if course:
                # Spring and Summer have the same acronym??
                year = course["year"][2:4]
                season = course["season"][0]
                string += " " + year + season
            else:
                string += " Leveling Course Marked Completed. Not Found on Transcript."

        return string



def courses_contains(courses, course_id):
    for course in courses:
        if course["course_id"] == course_id:
            return course

    return None
