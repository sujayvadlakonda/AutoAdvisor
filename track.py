from requirement import SimpleRequirement, MultiRequirement
from course import LevelingCourse


class Track:
    def __init__(self):
        self.core_requirements = []
        self.leveling_courses = []


class ComputerScience:
    def __init__(self):
        self.leveling_courses = [
            LevelingCourse("CS 2340"),
            LevelingCourse("CS 5303"),
            LevelingCourse("CS 5333"),
            LevelingCourse("CS 5343"),
            LevelingCourse("CS 5348"),
        ]


class DataScience(ComputerScience):
    def __init__(self):
        super().__init__()

        self.core_requirements = [
            SimpleRequirement("CS 6313"),
            SimpleRequirement("CS 6350"),
            SimpleRequirement("CS 6363"),
            SimpleRequirement("CS 6375"),
            MultiRequirement(["CS 6301", "CS 6320", "CS 6327", "CS 6347", "CS 6360"]),
        ]

        self.leveling_courses.append(LevelingCourse("CS 3341"))
