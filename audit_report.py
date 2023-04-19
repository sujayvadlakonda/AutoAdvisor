import os

from transcript import Transcript
from course import Courses
from track import DataScience


class AuditReport:
    def __init__(self, transcript, track):
        courses = transcript.get_courses()
        courses = Courses(courses)
        self.courses = courses
        self.track = track

    def print_core(self):
        core = self._get_core_identifiers()
        print("Core Courses: ", end="")  # w/o new line
        print(", ".join(core))

    def print_electives(self):
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
