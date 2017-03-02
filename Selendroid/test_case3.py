# Android environment
import unittest
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] = 'Android Emulator'


APP_PATH = ""
# get absolute path relative to file


desired_caps['app'] = 'C:/WebDrivers/selendroid/my_test.apk'
# app package?
# driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# # iOS environment
# import unittest
# from appium import webdriver
#
# desired_caps = {}
# desired_caps['app'] = PATH('../../apps/UICatalog.app.zip')
#
# self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
