import os

from course_finder import get_courses
from course import Courses
from track import DataScience


class AuditReport:
    def __init__(self, path_to_transcript, track):
        courses = get_courses(path_to_transcript)
        courses = Courses(courses)
        self.courses = courses
        self.track = track

    def print_courses(self):
        self.print_core()
        self.print_electives()
        print()
        self.print_leveling()

    def print_core(self):
        core = self._get_core_identifiers()
        print("Core Courses: ", end="")  # w/o new line
        print(", ".join(core))

    def print_electives(self):
        print("Elective Courses: ", end="")  # w/o new line
        electives = self.track.get_electives(self.courses)

        ids = []
        for elective in electives:
            number = elective["course_id"].strip()
            subject = elective["subject"].strip()
            id = subject + " " + number
            ids.append(id)

        ids.sort()

        ids = ", ".join(ids)
        print(ids)

    def print_leveling(self):
        print("Leveling Courses and Pre-requisites from Admission Letter:")
        print()
        for leveling in self.track.leveling_courses:
            leveling.print()

    # Returns core courses on transcript regardless of completion status
    def _get_core_identifiers(self):
        core_courses = []

        for requirement in self.track.core_requirements:
            course_dict = requirement.is_met(self.courses)
            if course_dict:
                identifier = (
                    course_dict["subject"].strip()
                    + " "
                    + course_dict["course_id"].strip()
                )
                core_courses.append(identifier)

        return core_courses
