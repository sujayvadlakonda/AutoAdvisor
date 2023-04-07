class AuditReport:
    def __init__(self, courses, requirements):
        self.courses = []
        for course in courses:
            course_subject = course["subject"].strip()
            course_number = course["course_id"].strip()
            course_identifier = course_subject + " " + course_number
            self.courses.append(course_identifier)
        self.requirements = requirements

        self.requirements.fulfill(self.courses)

    def core_completed(self):
        return self.requirements.core


class Requirement:
    def fulfill(self, completed_courses):
        pass


class ExactRequirement(Requirement):
    def __init__(self, course):
        self.course = course

    def fulfill(self, completed_courses):
        # more pythonic way?
        if self.course in completed_courses:
            return self.course

        return False


class MultiRequirement(Requirement):
    def __init__(self, course_options):
        self.course_options = course_options

    def fulfill(self, completed_courses):
        for course in self.course_options:
            if course in completed_courses:
                return course

        return False


class Requirements:
    def __init__(self):
        self.requirements = []
        self.core = []
        self.electives = []
        self.unfulfilled_requirements = []

    def fulfill(self, completed_courses):
        for requirement in self.requirements:
            fulfilled_course = requirement.fulfill(completed_courses)
            if fulfilled_course:
                self.core.append(fulfilled_course)
            else:
                self.unfulfilled_requirements.append(requirement)


class DataScience(Requirements):
    def __init__(self):
        super().__init__()

        self.requirements = [
            ExactRequirement("CS 6313"),
            ExactRequirement("CS 6350"),
            ExactRequirement("CS 6363"),
            ExactRequirement("CS 6375"),
            MultiRequirement(["CS 6301", "CS 6320", "CS 6327", "CS 6347", "CS 6360"]),
        ]
