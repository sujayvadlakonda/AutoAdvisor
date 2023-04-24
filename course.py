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


class Courses:
    def __init__(self, courses=[]):
        self.courses = courses

    # Input: "CS 1234"
    def contains(self, course_identifier):
        for course in self.courses:
            identifier = course["course_id"]
            if identifier == course_identifier:
                return course

        return False
