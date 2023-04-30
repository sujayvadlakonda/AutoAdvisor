# This is where I read all the requirements from
# https://catalog.utdallas.edu/now/graduate/programs/ecs/computer-science
# https://catalog.utdallas.edu/now/graduate/programs/ecs/software-engineering

from requirement import SimpleRequirement, MultiRequirement
from course import LevelingCourse, courses_contains, _standardize_grade


class Track:
    def __init__(self):
        self.core_requirements = []
        self.leveling_courses = []
        self.name = ""


class ComputerScience:
    def __init__(self):
        self.leveling_courses = [
            LevelingCourse("CS 5303"),
            LevelingCourse("CS 5330"),
            LevelingCourse("CS 5333"),
            LevelingCourse("CS 5343"),
            LevelingCourse("CS 5348"),
        ]
        self.name = "Computer Science (Please Specialize!)"

    def get_electives(self, courses):
        electives = self._get_5xxx_electives(courses)
        consumed = self._get_core_consumed(courses)

        for course in courses:
            id = course["course_id"].strip()
            id_parts = id.split(" ")
            subject = id_parts[0]
            number = int(id_parts[1])
            if number >= 6000 and (subject == "CS" or subject == "SE"):
                id = subject + " " + str(number)
                if not id in consumed:
                    electives.append(course)

        return electives

    def _get_5xxx_electives(self, courses):
        electives = []

        cs5343 = courses_contains(courses, "CS 5343")
        cs5348 = courses_contains(courses, "CS 5348")
        cs5333 = courses_contains(courses, "CS 5333")

        # Add grade comparison some day
        if cs5343:
            electives.append(cs5343)
        if cs5348:
            electives.append(cs5348)
        if cs5333:
            electives.append(cs5333)

        electives.sort(key=lambda e: _standardize_grade(e["grade"]))

        return electives[0:1]

    def _get_core_consumed(self, courses):
        """
        Get the courses that are used to meet core requirements
        """
        consumed_courses = []

        for core_requirement in self.core_requirements:
            course = core_requirement.is_met(courses)
            if course:
                if isinstance(course, list):
                    for c in course:
                        consumed_courses.append(c)
                else:
                    consumed_courses.append(course)

        ids = []
        for course in consumed_courses:
            id = course["course_id"].strip()
            ids.append(id)

        return ids


class DataScience(ComputerScience):
    def __init__(self):
        super().__init__()

        self.name = "Data Science"

        self.core_requirements = [
            SimpleRequirement("CS 6313"),
            SimpleRequirement("CS 6350"),
            SimpleRequirement("CS 6363"),
            SimpleRequirement("CS 6375"),
            MultiRequirement(["CS 6301", "CS 6320", "CS 6327", "CS 6347", "CS 6360"]),
        ]

        self.leveling_courses.append(LevelingCourse("CS 3341"))


class CyberSecurity(ComputerScience):
    def __init__(self):
        super().__init__()

        self.name = "Cyber Security"

        self.core_requirements = [
            SimpleRequirement("CS 6324"),
            SimpleRequirement("CS 6363"),
            SimpleRequirement("CS 6378"),
            MultiRequirement(
                [
                    "CS 6332",
                    "CS 6348",
                    "CS 6349",
                    "CS 6377",
                ],
                n=2,
            ),
        ]
        self.leveling_courses.append(LevelingCourse("CS 5390"))


class IntelligentSystems(ComputerScience):
    def __init__(self):
        super().__init__()

        self.name = "Intelligent Systems"

        self.core_requirements = [
            SimpleRequirement("CS 6320"),
            SimpleRequirement("CS 6363"),
            SimpleRequirement("CS 6364"),
            SimpleRequirement("CS 6375"),
            MultiRequirement(["CS 6360", "CS 6378"]),
        ]


class InteractiveComputing(ComputerScience):
    def __init__(self):
        super().__init__()

        self.name = "Interactive Computing"

        self.core_requirements = [
            SimpleRequirement("CS 6326"),
            SimpleRequirement("CS 6363"),
            MultiRequirement(
                ["CS 6323", "CS 6328", "CS 6331", "CS 6334", "CS 6366"], n=3
            ),
        ]


class Network(ComputerScience):
    def __init__(self):
        super().__init__()

        self.name = "Networks and Telecommunications"

        self.core_requirements = [
            SimpleRequirement("CS 6352"),
            SimpleRequirement("CS 6363"),
            SimpleRequirement("CS 6378"),
            SimpleRequirement("CS 6385"),
            SimpleRequirement("CS 6390"),
        ]
        self.leveling_courses.append(LevelingCourse("CS 3341"))
        self.leveling_courses.append(LevelingCourse("CS 5390"))


class Systems(ComputerScience):
    def __init__(self):
        super().__init__()

        self.name = "Systems"

        self.core_requirements = [
            SimpleRequirement("CS 6304"),
            SimpleRequirement("CS 6363"),
            SimpleRequirement("CS 6378"),
            SimpleRequirement("CS 6396"),
            MultiRequirement(
                [
                    "CS 6349",
                    "CS 6376",
                    "CS 6380",
                    "CS 6397",
                ]
            ),
        ]


class Traditional(ComputerScience):
    def __init__(self):
        super().__init__()

        self.name = "Traditional Computer Science"

        self.core_requirements = [
            SimpleRequirement("CS 6363"),
            SimpleRequirement("CS 6378"),
            SimpleRequirement("CS 6390"),
            MultiRequirement(
                [
                    "CS 6353",
                    "CS 6360",
                    "CS 6371",
                ],
                n=2,
            ),
        ]

        self.leveling_courses.append(LevelingCourse("CS 5349"))
        self.leveling_courses.append(LevelingCourse("CS 5390"))


class SoftwareEngineering:
    def __init__(self):
        self.core_requirements = [
            SimpleRequirement("SE 6329"),
            SimpleRequirement("SE 6361"),
            SimpleRequirement("SE 6362"),
            SimpleRequirement("SE 6367"),
            SimpleRequirement("SE 6387"),
        ]
        self.leveling_courses = [LevelingCourse("SE 5354")]


# Data Science: Ted Lasso, Taylor Swift, Roy Kent, Krusty Krab, Monica Geller
# Intelligent Systems: Mike Modano, Stevie Budd, Keeley Jones
# Traditional Computer Science: Harry Potter
# Interactive Computing: Jamie Tartt, Ron Weasley
# Systems: Chandler Bing
# Software Engineering: Rachel Green
