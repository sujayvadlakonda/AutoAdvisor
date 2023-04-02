import unittest

from course_finder import get_courses

class TestCourseFinder(unittest.TestCase):
    def test_ted_lasso(self):
        self.assertEqual(len(get_courses("transcripts/ted-lasso.pdf")), 12)



unittest.main()
