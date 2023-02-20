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
