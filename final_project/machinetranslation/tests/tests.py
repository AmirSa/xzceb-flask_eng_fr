import unittest

from translator import english_to_french, french_to_english

class test_en2fr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello")["translations"][0]["translation"], "Bonjour") 

class test_fr2en(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english("Bonjour")["translations"][0]["translation"]
, "Hello") 


unittest.main()