import unittest
from selenium import webdriver


class searchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(
            executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
        self.driver.get("https://www.google.com/")
        print("Title of the page is :" + self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(
            executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
        self.driver.get("https://www.bing.com")
        print("Title of the page is :" + self.driver.title)
        self.driver.close()

    def test_screenshot(self):
        self.driver = webdriver.Chrome(
            executable_path="/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        print("Title of the page is :" + self.driver.title)
        self.driver.get_screenshot_as_file("/Users/chandrashekarbasavaraj/Downloads/sample.jpg")


if __name__ == "__main__":
    unittest.main()
