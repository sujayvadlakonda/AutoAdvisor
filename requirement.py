from course import courses_contains, _compare_grade, _standardize_grade


class Requirement:
    def is_met(self, completed_courses):
        pass


class SimpleRequirement(Requirement):
    def __init__(self, course):
        self.course = course

    def is_met(self, courses):
        return courses_contains(courses, self.course)


class MultiRequirement(Requirement):
    def __init__(self, options, n=1):
        self.options = options
        self.n = n

    def is_met(self, courses):
        """
        Return the course with the highest grade that meets an option.
        If mulitple courses meet, pick the one that comes first in self.options.
        """
        array = []

        for option in self.options:
            course = courses_contains(courses, option)
            if course:
                array.append(course)

        array.sort(key=lambda c: _standardize_grade(c["grade"]))

        return array[0:self.n]
