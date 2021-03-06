import os
from time import sleep
import unittest

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# think times can be useful e.g. when testing with an emulator
THINK_TIME = 5.

class SimpleSalendroidTests(unittest.TestCase):
    def setUp(self):
        app_location = r"C:\WebDrivers\appium"
        app_name = "ApiDemos-debug.apk"
        device_name = "4df71cef65503121"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['automationName'] = "selendroid"
        desired_caps['app'] = os.path.join(app_location, app_name)

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_selendroid(self):
        el = self.driver.find_element_by_name("Animation")
        # assert el.text == "Animation"
        self.assertEqual('Animation', el.text)

        el = self.driver.find_element_by_class_name("android.widget.TextView")
        # assert el.text == "Accessibility"
        self.assertEqual('Accessibility', el.text)

        el = self.driver.find_element_by_name("App")
        el.click()
        sleep(THINK_TIME)

        els = self.driver.find_elements_by_class_name("android.widget.TextView")
        # Selendroid gets all the elements, not just the visible ones
        self.assertLessEqual(14, len(els))

        self.driver.find_element_by_name('Action Bar')

        self.driver.back()
        sleep(THINK_TIME)

        el = self.driver.find_element_by_name("Animation")
        self.assertEqual('Animation', el.text)

suite = unittest.loader.findTestCases(__file__)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleSalendroidTests)
unittest.TextTestRunner(verbosity=2).run(suite)