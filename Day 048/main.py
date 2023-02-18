from time import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

timeout = time() + 5
five_min = time() + 60 * 5
chrome_driver_path = "~/ws/chromedriver"
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)
URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)

cookie = driver.find_element(by=By.ID, value="cookie")

while True:
    cookie.click()
    if time() > timeout:
        to_buy = []
        shopping_cart = driver.find_elements(by=By.CSS_SELECTOR,
                                             value="#store div")
        for item in shopping_cart[:-1]:
            if item.get_attribute("class") != "grayed":
                to_buy.append(item)
        to_buy[-1].click()
        timeout = time() + 5
        if time() > five_min:
            print(driver.find_element(By.ID, value="cps").text)
            break
