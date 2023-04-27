from course_finder import get_courses


class AuditReport:
    def __init__(self, path_to_transcript, track):
        courses = get_courses(path_to_transcript)
        self.courses = courses
        self.track = track

    def get_courses_section(self):
        courses_section = ""
        courses_section += self.get_core_section() + "\n"
        courses_section += self.get_electives_section() + "\n\n"
        courses_section += self.get_leveling_section() + "\n"
        return courses_section

    def get_core_section(self):
        core_section = "Core Courses: "
        core = self._get_core_identifiers()
        core = ", ".join(core)
        core_section += core
        return core_section

    def get_electives_section(self):
        electives_section = "Elective Courses: "
        ids = self._get_electives()
        ids = ", ".join(ids)
        electives_section += ids
        return electives_section

    def get_leveling_section(self):
        leveling_section = (
            "Leveling Courses and Pre-requisites from Admission Letter:\n"
        )

        for leveling in self.track.leveling_courses:
            leveling_section += leveling.to_string(self.courses) + "\n"

        return leveling_section

    # Returns core courses on transcript regardless of completion status
    def _get_core_identifiers(self):
        core_courses = []

        for requirement in self.track.core_requirements:
            course_dict = requirement.is_met(self.courses)
            if course_dict:
                identifier = course_dict["course_id"]
                core_courses.append(identifier)

        return core_courses

    def _get_electives(self):
        electives = self.track.get_electives(self.courses)

        ids = []
        for elective in electives:
            id = elective["course_id"]
            ids.append(id)

        ids.sort()
        return ids
