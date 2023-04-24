class LevelingCourseStatus:
    COMPLETED = "Completed"
    WAIVED = "Waived"
    NOT_REQUIRED = "Not required by plan or elective"
    OTHER = "Other"


class LevelingCourse():
    def __init__(self, id, status=LevelingCourseStatus.COMPLETED):
        self.id = id
        self.status = status

    def print(self):
        print(self.id, self.status)

    def __str__(self):
        return self.id + " " + self.status

def courses_contains(courses, course_id):
    for course in courses:
        if course["course_id"] == course_id:
            return course

    return None
