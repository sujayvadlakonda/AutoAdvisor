class Track:
    def __init__(self):
        self.core_requirements = []
        self.core = []
        self.electives = []
        self.unfulfilled_requirements = []

    def fulfill(self, completed_courses):
        for requirements in self.core:
            pass
        for requirements in self.electives:
            pass
        for requirement in self.requirements:
            fulfilled_course = requirement.fulfill(completed_courses)
            if fulfilled_course:
                self.core.append(fulfilled_course)
            else:
                self.unfulfilled_requirements.append(requirement)


class DataScience(Track):
    def __init__(self):
        super().__init__()

        self.core_requirements = [
            ExactRequirement("CS 6313"),
            ExactRequirement("CS 6350"),
            ExactRequirement("CS 6363"),
            ExactRequirement("CS 6375"),
            MultiRequirement(["CS 6301", "CS 6320", "CS 6327", "CS 6347", "CS 6360"]),
        ]
