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
