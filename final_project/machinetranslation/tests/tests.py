"""This Module contains tests for the language translator"""
import unittest
from translator import english_to_french, french_to_english


class LanguageConvertion(unittest.TestCase):
    """Class for testing language translator"""

    def test_english_to_french(self):
        """Test From english to french"""
        self.assertEqual(english_to_french('hello'), 'Bonjour')
        self.assertIsNone(english_to_french(None))

    def test_french_to_english(self):
        """Test For french to english"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertIsNone(french_to_english(None))


if __name__ == '__main__':
    unittest.main()
