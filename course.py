class LevelingCourseStatus:
    COMPLETED = "Completed"
    WAIVED = "Waived"
    NOT_REQUIRED = "Not required by plan or elective"
    OTHER = "Other"


class LevelingCourse:
    def __init__(self, id, status=LevelingCourseStatus.COMPLETED):
        self.id = id
        self.status = status

    def gui_to_string(self):
        displayed_class = self.id

        return displayed_class

    def to_string(self, courses):
        string = self.id + " " + self.status

        if self.status == LevelingCourseStatus.COMPLETED:
            course = courses_contains(courses, self.id)
            if course:
                # Spring and Summer have the same acronym??
                year = course["year"][2:4]
                season = course["season"][0]
                string += " " + year + season
            else:
                string += " Leveling Course Marked Completed. Not Found on Transcript."

        return string


def courses_contains(courses, course_id):
    for course in courses:
        if course["course_id"] == course_id:
            return course

    return None


def _compare_grade(a, b):
    """
    An absolute hack, used to pick the higher grade.
    a and b are expected to be like A+ or None.
    If a and b are equal, return True.
    If a is a higher grade return True.
    If b is a higher grade return False.

    This works by changing A+ to AA, A to AB and A- to AC.
    None is an edge case for courses in progress.
    """
    a = _standardize_grade(a)
    b = _standardize_grade(b)

    if b == None:
        return 1
    if a == None:
        return -1

    return a < b


def _standardize_grade(grade):
    """Implements the hack described in self._compare_grade()"""
    if grade == None:
        return "ZZZZ"

    grade = grade.strip()
    if len(grade) == 1:
        return grade + "B"
    elif grade[1] == "+":
        return grade[0] + "A"
    elif grade[1] == "-":
        return grade[0] + "C"

    raise Exception("Tried to standardize %s", grade)