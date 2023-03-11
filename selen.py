import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# indicate which web browser driver to use 

driver = webdriver.Chrome()
driver.get('https://music.163.com/#/playlist?id=2313062981')

actions = ActionChains(driver)
element = driver.find_element(By.linkText("登录"));

actions.move_to_element(element).click()

element = driver.find_element(By.linText('选择其他登录模式'))
actions.move_to_element(element).click()