import os
import time
from appium import webdriver

app_location = r"C:\WebDrivers\appium"
app_name = "selendroid-test-app-0.17.0.apk"
device_name = "192.168.0.148:5555"
app_path = os.path.join(app_location, app_name)

capabilities = {
  'platformName': 'Android',
  'platformVersion': '4.4.2',
  'deviceName': device_name,
  'app': app_path,
  'appPackage': 'io.selendroid.testapp',
  'appActivity': '.HomeScreenActivity'
}

def test_confirmation_popup():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
    try:
        end = driver.find_element_by_id("io.selendroid.testapp:id/buttonTest")
        end.click()
        driver.find_element_by_xpath("//android.widget.Button[@text='No, no']").click()
        assert end.is_displayed()
    finally:
        driver.quit()

def test_input_text():
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
    try:
        el = driver.find_element_by_xpath("//android.widget.EditText[@content-desc='my_text_fieldCD']")
        driver.set_value(el, 'Testing')
        text = el.get_attribute('text')
        assert 'Testing' == text
        # fails because: Testing. Editing.
    finally:
        driver.quit()


