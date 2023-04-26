from course import courses_contains


class Requirement:
    def is_met(self, completed_courses):
        pass


class SimpleRequirement(Requirement):
    def __init__(self, course):
        self.course = course

    def is_met(self, courses):
        return courses_contains(courses, self.course)


class MultiRequirement(Requirement):
    def __init__(self, options):
        self.options = options

    def is_met(self, courses):
        """
        Return the course with the highest grade that meets an option.
        If mulitple courses meet, pick the one that comes first in self.options.
        """
        best_course = None
        best_grade = None

        for option in self.options:
            course = courses_contains(courses, option)
            if course:
                if not self._compare_grade(best_grade, course["grade"]):
                    best_course = course
                    best_grade = course["grade"]
                if best_course == None:
                    best_course = course
                    best_grade = course["grade"]

        return best_course

    def _compare_grade(self, a, b):
        """
        An absolute hack, used to pick the higher grade.
        a and b are expected to be like A+ or None.
        If a and b are equal, return True.
        If a is a higher grade return True.
        If b is a higher grade return False.

        This works by changing A+ to AA, A to AB and A- to AC.
        None is an edge case for courses in progress.
        """
        a = self._standardize_grade(a)
        b = self._standardize_grade(b)

        if b == None:
            return True
        if a == None:
            return False

        return a < b

    def _standardize_grade(self, grade):
        """Implements the hack described in self._compare_grade()"""
        if grade == None:
            return grade

        grade = grade.strip()
        if len(grade) == 1:
            return grade + "B"
        elif grade[1] == "+":
            return grade[0] + "A"
        elif grade[1] == "-":
            return grade[0] + "C"

        raise Exception("Tried to standardize %s", grade)
