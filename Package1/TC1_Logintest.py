import unittest


class Logintest(unittest.TestCase):
    def test_loginbyemail(self):
        print("This is email login")
        self.assertTrue(True)

    def test_loginbyfb(self):
        print("This is fb login")
        self.assertTrue(True)

    def test_twitter(self):
        print("This is twitter login")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
