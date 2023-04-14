class Requirement:
    def is_met(self, completed_courses):
        pass


class SimpleRequirement(Requirement):
    def __init__(self, course):
        self.course = course

    def is_met(self, courses):
        return courses.contains(self.course)


class MultiRequirement(Requirement):
    def __init__(self, options):
        self.options = options

    def is_met(self, courses):
        for option in self.options:
            course = courses.contains(option)
            if course:
                return course

        return False
