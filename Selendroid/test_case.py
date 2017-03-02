"""
Qxf2 Services: Sample Python script to get started with Selendroid
"""
import unittest, time
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions


class FindElementTest(unittest.TestCase):

    def setUp(self):
        "Set up the Android Driver"
        self.driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.ANDROID)
        self.driver.implicitly_wait(30)

    def test_Launch_Chessdom(self):
        "Test the title of the Chess News page on Chessdom.com is correct"
        # Go to url:http://www.chessdom.com/
        self.driver.get('http://www.chessdom.com/')
        time.sleep(5)

        #Click on the link "Chess News"
        ChessNews = self.driver.find_element_by_xpath("//a[@title='View all posts filed under Chess News' and text()='Chess News']")
        ChessNews.click()
        time.sleep(5) #Increase sleep time if your emulator has performance issues

        # Assert that the Page has title "Chess News | Chessdom"
        self.assertIn("Chess News | Chessdom", self.driver.title)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()