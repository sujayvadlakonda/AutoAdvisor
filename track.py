# This is where I read all the requirements from
# https://catalog.utdallas.edu/2021/graduate/programs/ecs/computer-science

from requirement import SimpleRequirement, MultiRequirement
from course import LevelingCourse, courses_contains


class Track:
    def __init__(self):
        self.core_requirements = []
        self.leveling_courses = []
        self.name = ""


class ComputerScience:
    def __init__(self):
        self.leveling_courses = [
            LevelingCourse("CS 2340"),
            LevelingCourse("CS 5303"),
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
            subject = id[0:2]
            number = int(id[3:7])
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
            electives.add(cs5343)
        elif cs5348:
            electives.add(cs5348)
        elif cs5333:
            electives.add(cs5333)

        return electives

    def _get_core_consumed(self, courses):
        """
        Get the courses that are used to meet core requirements
        """
        consumed_courses = []

        for core_requirement in self.core_requirements:
            course = core_requirement.is_met(courses)
            if course:
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


# Data Science: Ted Lasso, Taylor Swift, Roy Kent, Krusty Krab, Monica Geller
# Intelligent Systems: Mike Modano, Stevie Budd
# Traditional Computer Science: Harry Potter
# Interactive Computing: Jamie Tartt, Ron Weasley
# Systems: Chandler Bing
# Software Engineering: Rachel Green
