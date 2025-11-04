import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
    

    def test_multiple_words(self):

        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()




''' def test_multiple_words was set to fail on purpose. The function found in cap.py would onlt capitalize the first letter for the first word. 
In order for this to work we'd have to change the cap_text function from .capitlize to .title. '''