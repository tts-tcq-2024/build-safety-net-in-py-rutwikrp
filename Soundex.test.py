import unittest
from Soundex import compute_soundex

class SoundexTest(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(compute_soundex(""), "")
    
    def test_single_letter(self):
        self.assertEqual(compute_soundex("A"), "A000")
    
    def test_basic_examples(self):
        self.assertEqual(compute_soundex("Robert"), "R163")
        self.assertEqual(compute_soundex("Rupert"), "R163")
        self.assertEqual(compute_soundex("Rubin"), "R150")
        self.assertEqual(compute_soundex("Ashcraft"), "A261")
        self.assertEqual(compute_soundex("Ashcroft"), "A261")
        self.assertEqual(compute_soundex("Pfister"), "P236")

if __name__ == '__main__':
    unittest.main()
