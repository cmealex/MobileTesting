import os
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ComplexAndroidTests(unittest.TestCase):
    def setUp(self):
        app_location = r"C:\WebDrivers\appium"
        app_name = "ApiDemos-debug.apk"
        device_name = "192.168.0.14:5555"
        # device_name = "4df71cef65503121"

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = device_name
        desired_caps['app'] = os.path.join(app_location, app_name)

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_smiley_face(self):
        # just for the fun of it.
        # this doesn't really assert anything.
        self.driver.find_element_by_accessibility_id('Graphics').click()

        els = self.driver.find_elements_by_class_name('android.widget.TextView')
        self.driver.scroll(els[len(els)-1], els[0])

        action = TouchAction(self.driver)
        el = self.driver.find_element_by_accessibility_id('Touch Paint')
        action.tap(el).perform()
        # el.click()

        positions = []
        positions.append((100, 200))
        positions.append((100, 400))

        self.driver.tap(positions)
        # so you can see it
        sleep(10)
        self.driver.press_keycode(3)
        print 'still'
suite = unittest.loader.findTestCases(__file__)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ComplexAndroidTests)
unittest.TextTestRunner(verbosity=2).run(suite)