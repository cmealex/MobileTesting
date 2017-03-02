from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.ANDROID)
driver.get("http://google.com")
driver.switch_to.window('NATIVE_APP')
driver.find_element(By.ID, 'buttonTest')

from selenium.webdriver.common.action_chains import ActionChains
""" Instantiate the driver like: driver = driver=webdriver.Remote( ... ); """
chain = ActionChains(driver)
""" Send search key"""
chain.send_keys(u'\ue103').perform()