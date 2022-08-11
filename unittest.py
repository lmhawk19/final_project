import unittest
from unittest.mock import patch

from output_feature import words_of_affirmation,physical_touch,quality_time,acts_of_service,gift_giving,love_language_randomizer

class Test_woa(unittest.TestCase):
    @patch("builtins.input",side_effect[ans1,ans2,ans3])
    def test_language(self, mock_inputs):
        ans1 = "words of affirmation"
        ans2 = "yes"
        ans3 = "yes"
        result = words_of_affirmation()
        self.assertEqual(result,ans1,ans2,ans3)  # add assertion here


if __name__ == '__main__':
    unittest.main()