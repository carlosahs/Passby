import unittest

from passby import search_char_type

class TestSearchCharType(unittest.TestCase):
    def test_search_digits(self):
        self.assertEqual("digits", search_char_type("1"), 
                         "Should be 'digits'")
        self.assertEqual("digits", search_char_type("5"), 
                         "Should be 'digits'")     
        self.assertEqual("digits", search_char_type("9"), 
                         "Should be 'digits'")   
    def test_search_lowercases(self):
        self.assertEqual("lowercases", search_char_type("a"), 
                         "Should be 'digits'")
        self.assertEqual("lowercases", search_char_type("r"), 
                         "Should be 'digits'")     
        self.assertEqual("lowercases", search_char_type("x"), 
                         "Should be 'digits'") 

if __name__ == "__main__":
    unittest.main()     