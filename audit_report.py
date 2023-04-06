class AuditReport:
    def __init__(self, courses, requirements):
        self.courses = courses
        self.requirements = requirements

    def get_core_fulfilled(self):
        core_fulfilled = []

        for course in self.courses:
            course_full_id = (
                course["subject"].strip() + " " + course["course_id"].strip()
            )
            if self.requirements.is_requirement(course_full_id):
                core_fulfilled.append(course_full_id)

        return core_fulfilled


class CoreRequirements:
    requirements = []

    def is_requirement(self, course):
        if course in self.requirements:
            return True

        return False


class DataScience(CoreRequirements):
    requirements = [
        "CS 6313",
        "CS 6350",
        "CS 6363",
        "CS 6375",
        ["CS 6301", "CS 6320", "CS 6327", "CS 6347", "CS 6360"],
    ]
