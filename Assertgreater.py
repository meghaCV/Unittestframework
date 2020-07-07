import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        # self.assertgreater
        # self.assertGreater(100, 10)  # first value should be greater than second,it returns true
        # self.assertGreaterEqual(100, 101)  # first value should be greater than second or atleast equal to second
        # self.assertLess(10, 100)#first value should be lesser than second,it returns true
        self.assertLessEqual(10, 10)  # first value should be lesser than second or atleast equal to second


if __name__ == "__main__":
    unittest.main()
