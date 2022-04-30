import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):         
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Two"), "Deux")
        self.assertNotEqual(english_to_french("One"), "Deux")        


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):        
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Deux"), "Two")
        self.assertNotEqual(french_to_english("Deux"), "One")
        

unittest.main()