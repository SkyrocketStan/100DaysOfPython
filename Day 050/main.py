import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

FB_EMAIL = os.getenv("app.email")
FB_PASSWORD = os.getenv("app.pass")

driver = webdriver.Chrome()

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(by=By.XPATH, value='//*[@id="c-1351236777"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

sleep(2)
fb_login = driver.find_element(by=By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()