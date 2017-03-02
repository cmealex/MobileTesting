import os
import time

from appium import webdriver

def test_calc():
    app_location = r"C:\WebDrivers\appium"
    # app_name = "Calculator_2.0.apk"
    device_name = "192.168.0.148:5555"
    desired_caps = {}
    desired_caps['browserName'] = ''
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = device_name
    desired_caps['appPackage'] = 'com.sec.android.app.popupcalculator'
    desired_caps['appActivity'] = 'com.sec.android.app.popupcalculator.Calculator'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    try:
        driver.find_element_by_id("com.sec.android.app.popupcalculator:id/bt_07").click()
        driver.find_element_by_id("com.sec.android.app.popupcalculator:id/bt_add").click()
        driver.find_element_by_id("com.sec.android.app.popupcalculator:id/bt_05").click()
        driver.find_element_by_id("com.sec.android.app.popupcalculator:id/bt_equal").click()
        actual = driver.find_element_by_class_name("android.widget.EditText")
        assert '12' == actual.text.split("=")[1].split(".")[0]
    finally:
        driver.quit()

def test_browser():
    device_name = "192.168.0.148:5555"
    desired_caps = {}
    desired_caps['browserName'] = 'Chrome'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = device_name
    desired_caps['appPackage'] = 'com.sec.android.app.launcher'
    desired_caps['appActivity'] = 'com.sec.android.app.launcher.Chrome'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    try:
        driver.get('http://google.com')
        inputElement = driver.find_element_by_name("q")
        inputElement.send_keys("cheese!")
        inputElement.submit()
        driver.save_screenshot("some.png")
    finally:
        driver.quit()