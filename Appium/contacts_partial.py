import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        app_location = r"C:\WebDrivers\appium"
        app_name = "ContactManager.apk"
        device_name = "4df71cef65503121"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = device_name
        desired_caps['app'] = os.path.join(app_location, app_name)
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = '.ContactManager'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        el = self.driver.find_element_by_accessibility_id("Add Contact")
        el.click()

        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("Appium User1")
        # textfields[2].send_keys("someone@appium.io")

        self.assertEqual('Appium User', textfields[0].text)
        # self.assertEqual('someone@appium.io', textfields[2].text)
        sleep(5)
        # self.driver.find_element_by_accessibility_id("Save").click()
        #
        # # for some reason "save" breaks things
        # alert = self.driver.switch_to_alert()
        #
        # # no way to handle alerts in Android
        # self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()
        #
        # self.driver.press_keycode(3)

suite = unittest.loader.findTestCases(__file__)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
unittest.TextTestRunner(verbosity=2).run(suite)