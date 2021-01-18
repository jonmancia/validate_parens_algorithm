import unittest
from main import valid_parentheses


class TestParensString(unittest.TestCase):

    def testParens1(self):
        string = "()()()"
        self.assertTrue(valid_parentheses(string), msg="Valid")

    def testParens2(self):
        string = ")(()))"
        self.assertFalse(valid_parentheses(string),
                         msg="Opening parens is invalid")

    def testParens3(self):
        string = "))(("
        self.assertFalse(valid_parentheses(string),
                         msg="Non-matching opening/closing parens")

    def testParens4(self):
        string = "()()()()())()("
        self.assertFalse(valid_parentheses(string),
                         msg="Incompatible opening and closing characters")

    def testNoParens(self):
        string = "Hello()()))(("
        self.assertFalse(valid_parentheses(string), msg="Invalid characters")


if __name__ == '__main__':
    unittest.main(verbosity=3)
