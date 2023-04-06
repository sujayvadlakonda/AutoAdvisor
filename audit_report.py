class AuditReport:
    def __init__(self, courses, requirements):
        self.courses = []
        for course in courses:
            course_subject = course["subject"].strip()
            course_number = course["course_id"].strip()
            course_identifier = course_subject + " " + course_number
            self.courses.append(course_identifier)
        self.requirements = requirements

    def get_requirements_fulfilled(self):
        return self.requirements.requirements_fulfilled(self.courses)



class Requirement:
    def fulfilled(self, courses):
        pass


class SimpleRequirement(Requirement):
    def __init__(self, course):
        self.course = course

    def fulfilled(self, courses):
        # more pythonic way?
        if self.course in courses:
            return self.course

        return False


class MultiRequirement(Requirement):
    def __init__(self, course_options):
        self.course_options = course_options


    def fulfilled(self, courses):
        for course in self.course_options:
            if course in courses:
                return course

        return False


class Requirements:
    requirements = []

    def requirements_fulfilled(self, courses):
        requirements_fulfilled = []

        for requirement in self.requirements:
            fulfilled_course = requirement.fulfilled(courses)
            if fulfilled_course:
                requirements_fulfilled.append(fulfilled_course)

        return requirements_fulfilled


class DataScience(Requirements):
    requirements = [
        SimpleRequirement("CS 6313"),
        SimpleRequirement("CS 6350"),
        SimpleRequirement("CS 6363"),
        SimpleRequirement("CS 6375"),
        MultiRequirement(["CS 6301", "CS 6320", "CS 6327", "CS 6347", "CS 6360"]),
    ]
