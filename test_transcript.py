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
        self.harry_potter = Transcript("transcripts/harry-potter.pdf")
        self.ron_weasley = Transcript("transcripts/ron-weasley.pdf")
        self.jaime_tartt = Transcript("transcripts/jaime-tartt.pdf")

    def test_name(self):
        self.assertEqual(self.ted_lasso.get_name(), "Ted Lasso")
        self.assertEqual(self.mike_modano.get_name(), "Mike Modano")
        self.assertEqual(self.taylor_swift.get_name(), "Taylor Swift")
        self.assertEqual(self.roy_kent.get_name(), "Roy Kent")
        self.assertEqual(self.stevie_budd.get_name(), "Stevie Budd")
        self.assertEqual(self.krusty_krab.get_name(), "Krusty Krab")
        self.assertEqual(self.keeley_jones.get_name(), "Keeley Jones")
        self.assertEqual(self.harry_potter.get_name(), "Harry Potter")
        self.assertEqual(self.ron_weasley.get_name(), "Ron Weasley")
        self.assertEqual(self.jaime_tartt.get_name(), "Jaime Tartt")

    def test_id(self):
        self.assertEqual(self.ted_lasso.get_id(), "2021504218")
        self.assertEqual(self.mike_modano.get_id(), "2021543217")
        self.assertEqual(self.taylor_swift.get_id(), "2021012398")
        self.assertEqual(self.roy_kent.get_id(), "2021231140")
        self.assertEqual(self.stevie_budd.get_id(), "2021261148")
        self.assertEqual(self.krusty_krab.get_id(), "2021122928")
        self.assertEqual(self.keeley_jones.get_id(), "2021244212")
        self.assertEqual(self.harry_potter.get_id(), "2021316125")
        self.assertEqual(self.ron_weasley.get_id(), "2021324553")
        self.assertEqual(self.jaime_tartt.get_id(), "2021322330")

    def test_major(self):
        self.assertEqual(self.ted_lasso.get_major(), "Computer Science Major")
        self.assertEqual(self.mike_modano.get_major(), "Computer Science Major")
        self.assertEqual(self.taylor_swift.get_major(), "Computer Science Major")
        self.assertEqual(self.roy_kent.get_major(), "Computer Science Major")
        self.assertEqual(self.stevie_budd.get_major(), "Computer Science Major")
        self.assertEqual(self.krusty_krab.get_major(), "Computer Science Major")
        self.assertEqual(self.keeley_jones.get_major(), "Computer Science Major")
        self.assertEqual(self.harry_potter.get_major(), "Computer Science Major")
        self.assertEqual(self.ron_weasley.get_major(), "Computer Science Major")
        self.assertEqual(self.jaime_tartt.get_major(), "Computer Science Major")

    def test_beginning_of_graduate_record(self):
        self.assertEqual(self.ted_lasso.get_beginning_of_graduate_record(), "2021 Fall")
        self.assertEqual(
            self.mike_modano.get_beginning_of_graduate_record(), "2021 Fall"
        )
        self.assertEqual(
            self.taylor_swift.get_beginning_of_graduate_record(), "2021 Fall"
        )
        self.assertEqual(self.roy_kent.get_beginning_of_graduate_record(), "2021 Fall")
        self.assertEqual(
            self.stevie_budd.get_beginning_of_graduate_record(), "2021 Fall"
        )
        self.assertEqual(
            self.krusty_krab.get_beginning_of_graduate_record(), "2021 Fall"
        )
        self.assertEqual(
            self.keeley_jones.get_beginning_of_graduate_record(), "2022 Fall"
        )
        self.assertEqual(
            self.harry_potter.get_beginning_of_graduate_record(), "2021 Fall"
        )
        self.assertEqual(
            self.ron_weasley.get_beginning_of_graduate_record(), "2021 Fall"
        )
        self.assertEqual(
            self.jaime_tartt.get_beginning_of_graduate_record(), "2021 Fall"
        )

    def test_combined_cumulative_gpa(self):
        self.assertEqual(self.ted_lasso.get_combined_cumulative_gpa(), "3.709")
        self.assertEqual(self.mike_modano.get_combined_cumulative_gpa(), "3.571")
        self.assertEqual(self.taylor_swift.get_combined_cumulative_gpa(), "3.963")
        self.assertEqual(self.roy_kent.get_combined_cumulative_gpa(), "3.293")
        self.assertEqual(self.stevie_budd.get_combined_cumulative_gpa(), "3.481")
        self.assertEqual(self.krusty_krab.get_combined_cumulative_gpa(), "3.800")
        self.assertEqual(self.keeley_jones.get_combined_cumulative_gpa(), "3.953")
        self.assertEqual(self.harry_potter.get_combined_cumulative_gpa(), "3.234")
        self.assertEqual(self.ron_weasley.get_combined_cumulative_gpa(), "3.519")
        self.assertEqual(self.jaime_tartt.get_combined_cumulative_gpa(), "3.401")


unittest.main()
