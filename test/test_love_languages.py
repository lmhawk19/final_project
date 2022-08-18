import unittest
from love_languages import WordsOfAffirmation


class TestLoveLanguages(unittest.TestCase):
    def test_words_of_affirmation(self):
        words_of_affirmation = WordsOfAffirmation()
        self.assertEqual(words_of_affirmation.name, 'Words of affirmation')
        self.assertEqual(words_of_affirmation.description, 'Words of affirmation are words that effectively communicate your love, appreciation, and respect for your partner. People with words of affirmation as their love language value verbal acknowledgements of affection, compliments, words of appreciation, and verbal encouragement.')
        self.assertEqual(len(words_of_affirmation.get_random_suggestions()), 10)
