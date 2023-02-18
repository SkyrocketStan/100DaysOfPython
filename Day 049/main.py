import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

USERNAME = os.getenv("linkedin-user")
PASSWORD = os.getenv("linkedin-pass")

driver = webdriver.Chrome()
driver.get(URL)

sign_btn = driver.find_element(By.LINK_TEXT, "Sign in")
sign_btn.click()

email_input = driver.find_element(By.ID, "username")
email_input.send_keys(USERNAME)

email_input = driver.find_element(By.ID, "password")
email_input.send_keys(PASSWORD)

sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
sign_in_button.click()

time.sleep(10)
