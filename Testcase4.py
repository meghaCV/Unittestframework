import unittest


class AppTest(unittest.TestCase):

    def test_searchTest(self):
        print("This is my search test case")

    def test_prepaidTest(self):
        print("This is my prepaid test case")

    def test_gmailTest(self):
        print("This is my gmail test case")

    @unittest.SkipTest
    def test_googleTest(self):
        print("This is my google test case")

    @unittest.skipIf(1 == 1, "one is equal to one")
    def test_postTest(self):
        print("This is my post test case")

    @unittest.skip("I am skipping this because it is not ready")
    def test_advancedTest(self):
        print("This is my advanced test case")


if __name__ == "__main__":
    unittest.main()
