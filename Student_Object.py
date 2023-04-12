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
#       }, 'Traditional')
class Student:
    def __init__(self, student_id, name, program, major, courses, cumulative, transfer_cumulative, combined_cumulative, track):
        self.student_id = student_id
        self.name = name
        self.program = program
        self.major = major
        self.courses = courses
        self.cumulative = cumulative
        self.transfer_cumulative = transfer_cumulative
        self.combined_cumulative = combined_cumulative
        self.track = track


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


# Degree Plan data object
class DegreePlan:
    def __init__(self):
        data_science = {
            'Core Courses': ['CS 6313', 'CS 6350', 'CS 6363', 'CS 6375'],
            'One of the following Five Core Courses': ['CS 6301', 'CS 6320', 'CS 6327', 'CS 6347', 'CS 6360'],
            'Five Approved 6000 Level Electives': [],
            'Electives (3 credits minimum)': [],
            'Prerequisites': ['CS 5303', 'CS 5330', 'CS 5333', 'CS 5343', 'CS 5348', 'CS 3341']
        }
        systems = {
            'Core Courses': ['CS 6304', 'CS 6363', 'CS 6378', 'CS 6396'],
            'One of the following Courses': ['CS 6349', 'CS 6376', 'CS 6380', 'CS 6397', 'CS 6399'],
            'Five Approved 6000 Level Electives': [],
            'Electives (3 credits minimum)': [],
            'Prerequisites': ['CS 5303', 'CS 5330', 'CS 5333', 'CS 5343', 'CS 5348', 'CS 5390']
        }
        interactive_computing = {
            'Core Courses': ['CS 6326', 'CS 6363'],
            'Three of the following Five Core Courses': ['CS 6323', 'CS 6328', 'CS 6331', 'CS 6334', 'CS 6366'],
            'Five Approved 6000 Level Electives': [],
            'Electives (3 credits minimum)': [],
            'Prerequisites': ['CS 5303', 'CS 5330', 'CS 5333', 'CS 5343', 'CS 5348']
        }
        cyber_security = {
            'Core Courses': ['CS 6324', 'CS 6363', 'CS 6378'],
            'Two Courses from the following list': ['CS 6332', 'CS 6348', 'CS 6349', 'CS 6377'],
            'Two AI* Approved 6000 Level Electives': [],
            '': [],
            'Prerequisites': ['CS 5303', 'CS 5330', 'CS 5333', 'CS 5343', 'CS 5348', 'CS 5390']
        }
        intelligent_systems = {
            'Core Courses': ['CS 6320', 'CS 6363', 'CS 6364', 'CS 6375'],
            'One of the following Courses': ['CS 6360', 'CS 6378'],
            'Five Approved 6000 Level Electives': [],
            'Electives (3 credits minimum)': [],
            'Prerequisites': []
        }
