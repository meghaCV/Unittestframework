import unittest


def setUpmodule():#executed before any class or method is executed
    print("before the module")


def teardownmodule():#executed after everything present in the python module
    print("before the module")


class AppTest(unittest.TestCase):

    @classmethod
    def setUp(self):  # executed before the every method
        print("set up,pre requisite for all the definitions")

    @classmethod
    def tearDown(self):  # executed after the every method
        print("required at the end of every methods")

    @classmethod
    def setUpClass(cls):  # executed one time before beginning of class
        print("open application")

    @classmethod
    def tearDownClass(cls):  # executed one time after executing class
        print("close the application")

    def test_searchTest(self):
        print("This is my search test case")

    def test_prepaidTest(self):
        print("This is my prepaid test case")

    def test_postTest(self):
        print("This is my post test case")

    def test_advancedTest(self):
        print("This is my advanced test case")


if __name__ == "__main__":
    unittest.main()
