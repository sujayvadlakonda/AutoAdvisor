# Student data object
# ex: Student(2021316125, 'Harry Potter', 'Master', 'Computer Science', [course_object1, course_object2, ...],
#       {
#           'GPA': 3.234,
#           'Attempted': 33.0,
#           'Earned': 30.0,
#           'GPA_Uts': 30.0,
#           'Points': 97.02
#       },
#       {
#           'GPA': None,
#           'Attempted': 0.0,
#           'Earned': 0.0,
#           'GPA_Uts': 0.0,
#           'Points': 0.0
#       },
#       {
#           'GPA': 3.234,
#           'Attempted': 33.0,
#           'Earned': 30.0,
#           'GPA_Uts': 30.0,
#           'Points': 97.02
#       })
class Student:
    def __init__(self, student_id, name, program, major, courses, cumulative, transfer_cumulative, combined_cumulative):
        self.student_id = student_id
        self.name = name
        self.program = program
        self.major = major
        self.courses = courses
        self.cumulative = cumulative
        self.transfer_cumulative = transfer_cumulative
        self.combined_cumulative = combined_cumulative


# Course data object
# ex: Course('CS', 6360, 'DATABASE DESIGN', ['Murat Kantarcioglu', 'Mestan Firat Celiktug'], 3.0, 3.0, 'A-', 11.01)
class Course:
    def __init__(self, dept, code, name, attempted_credits, earned_credits, letter_grade, points):
        self.dept = dept
        self.code = code
        self.name = name
        self.attempted_credits = attempted_credits
        self.earned_credits = earned_credits
        self.letter_grade = letter_grade
        self.points = points
