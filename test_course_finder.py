import unittest

from transcript import Transcript

class TestCourseFinder(unittest.TestCase):
    def test_ted_lasso(self):
        transcript = Transcript("transcripts/ted-lasso.pdf")
        self.assertEqual(len(transcript.get_courses()), 12)



unittest.main()
