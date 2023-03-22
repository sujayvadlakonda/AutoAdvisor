import unittest

from transcript import Transcript


class TestTranscript(unittest.TestCase):
    def setUp(self):
        self.ted_lasso = Transcript("transcripts/ted-lasso.pdf")
        self.mike_modano = Transcript("transcripts/mike-modano.pdf")
        self.taylor_swift = Transcript("transcripts/taylor-swift.pdf")
        self.roy_kent = Transcript("transcripts/roy-kent.pdf")
        self.stevie_budd = Transcript("transcripts/stevie-budd.pdf")
        self.krusty_krab = Transcript("transcripts/krusty-krab.pdf")
        self.keeley_jones = Transcript("transcripts/keeley-jones.pdf")


    def test_student_name(self):
        self.assertEqual(self.ted_lasso.get_student_name(), "Ted Lasso")
        self.assertEqual(self.mike_modano.get_student_name(), "Mike Modano")
        self.assertEqual(self.taylor_swift.get_student_name(), "Taylor Swift")
        self.assertEqual(self.roy_kent.get_student_name(), "Roy Kent")
        self.assertEqual(self.stevie_budd.get_student_name(), "Stevie Budd")
        self.assertEqual(self.krusty_krab.get_student_name(), "Krusty Krab")
        self.assertEqual(self.keeley_jones.get_student_name(), "Keeley Jones")


    def test_student_id(self):
        self.assertEqual(self.ted_lasso.get_student_id(), "2021504218")
        self.assertEqual(self.mike_modano.get_student_id(), "2021543217")
        self.assertEqual(self.taylor_swift.get_student_id(), "2021012398")
        self.assertEqual(self.roy_kent.get_student_id(), "2021231140")
        self.assertEqual(self.stevie_budd.get_student_id(), "2021261148")
        self.assertEqual(self.krusty_krab.get_student_id(), "2021122928")
        self.assertEqual(self.keeley_jones.get_student_id(), "2021244212")



unittest.main()
