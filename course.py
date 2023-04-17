# Add parameters iff they are used somewhere
class Course:
    # id should be "CS 1234"
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return self.id


class LevelingCourseStatus:
    COMPLETED = "Completed"
    WAIVED = "Waived"
    NOT_REQUIRED = "Not required by plan or elective"
    OTHER = "Other"


class LevelingCourse(Course):
    def __init__(self, id, status=LevelingCourseStatus.COMPLETED):
        super().__init__(id)
        self.status = status

    def print(self):
        print(self.id, self.status)


class Courses:
    def __init__(self, courses=[]):
        self.courses = courses

    # Input: "CS 1234"
    def contains(self, course_identifier):
        for course in self.courses:
            identifier = course["subject"].strip() + " " + course["course_id"].strip()
            if identifier == course_identifier:
                return course

        return False
