# An abstract class. Basically a requirement class must have a fulfill method.
class Requirement:
    # This method should return the course that fulfills this Requirement
    # If no such course exists it should return false
    # Better name *highly* welcome
    def fulfill(self, completed_courses):
        pass


# A requirement that is fulfilled by exactly one course
# Better name ideas are welcome
class ExactRequirement(Requirement):
    def __init__(self, course):
        self.course = course

    def fulfill(self, completed_courses):
        # more pythonic way?
        if self.course in completed_courses:
            return self.course

        return False


# A requirement that is fulfilled by one of several courses
class MultiRequirement(Requirement):
    def __init__(self, course_options):
        self.course_options = course_options

    def fulfill(self, completed_courses):
        for course in self.course_options:
            if course in completed_courses:
                return course

        return False
