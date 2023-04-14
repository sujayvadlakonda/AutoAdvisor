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
