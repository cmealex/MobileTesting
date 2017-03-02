import os
import unittest
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys

from appium import webdriver

PLATFORM_VERSION = '4.4.2'


class AndroidWebViewTests(unittest.TestCase):

    def setUp(self):
        app_location = r"C:\WebDrivers\appium"
        app_name = "selendroid-test-app-0.17.0.apk"
        device_name = "192.168.0.148:5555"
        app_path = os.path.join(app_location, app_name)
        # app = os.path.abspath(
        #         os.path.join(os.path.dirname(__file__),
        #                      '../../apps/selendroid-test-app.apk'))
        desired_caps = {
            'app': app_path,
            'appPackage': 'io.selendroid.testapp',
            'appActivity': '.HomeScreenActivity',
            'platformName': 'Android',
            'platformVersion': PLATFORM_VERSION,
            'deviceName': device_name
        }

        if (PLATFORM_VERSION != '4.4'):
            desired_caps['automationName'] = 'selendroid'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',
                                       desired_caps)

    def test_webview(self):
        if (PLATFORM_VERSION == '4.4'):
            button = self.driver.find_element_by_accessibility_id('buttonStartWebviewCD')
        else:
            button = self.driver.find_element_by_name('buttonStartWebviewCD')
        button.click()
        sleep(1)
        self.driver.switch_to.context('WEBVIEW_0')

        input_field = self.driver.find_element_by_id('name_input')
        sleep(1)
        attrs = self.driver.execute_script(
            'var items = {};'
            ' for (index = 0; index < arguments[0].attributes.length; ++index) { '
            'items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
            input_field)
        # action = TouchAction(self.driver)
        # action.long_press(input_field).perform()  not working
        # https://github.com/appium/appium/issues/7063
        self.driver.keyevent("22")
        self.driver.keyevent("67")

        input_field.send_keys('Appium User')
        input_field.submit()
        # # test that everything is a-ok
        source = self.driver.page_source
        self.assertNotEqual(-1, source.find('This is my way of saying hello'))
        self.assertNotEqual(-1, source.find('"Appium User"'))
        sleep(3)

    def tearDown(self):
        self.driver.quit()

suite = unittest.loader.findTestCases(__file__)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidWebViewTests)
unittest.TextTestRunner(verbosity=2).run(suite)