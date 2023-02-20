import time

from selenium import webdriver

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()


def get_internet_speed(self):
    self.driver.get("https://www.speedtest.net/")

    # Depending on your location, you might need to accept the GDPR pop-up.
    # accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
    # accept_button.click()

    time.sleep(3)
    go_button = self.driver.find_element_by_css_selector(".start-button a")
    go_button.click()

    time.sleep(60)
    self.up = self.driver.find_element_by_xpath(
        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    self.down = self.driver.find_element_by_xpath(
        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
