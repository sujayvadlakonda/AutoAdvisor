from requirement import SimpleRequirement, MultiRequirement


class Track:
    def __init__(self):
        self.core_requirements = []


class DataScience(Track):
    def __init__(self):
        self.core_requirements = [
            SimpleRequirement("CS 6313"),
            SimpleRequirement("CS 6350"),
            SimpleRequirement("CS 6363"),
            SimpleRequirement("CS 6375"),
            MultiRequirement(["CS 6301", "CS 6320", "CS 6327", "CS 6347", "CS 6360"]),
        ]
