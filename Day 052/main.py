from selenium import webdriver

CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
SIMILAR_ACCOUNT = "INSTAGRAM ACCOUNT YOU WANT TO BECOME"
USERNAME = "YOUR INSTAGRAM EMAIL"
PASSWORD = "YOUR INSTAGRAM PASSWORD"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
