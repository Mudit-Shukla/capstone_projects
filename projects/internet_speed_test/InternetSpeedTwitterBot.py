from selenium import webdriver
import time

CHROME_DRIVER_PATH = "D:/python programs/Development/chromedriver"
URL_OF_SPEEDTEST = "https://www.speedtest.net/"
URL_OF_TWITTER = "https://twitter.com/login/"
PROMISED_DOWNLOAD = 30.00
PROMISED_UPLOAD = 30.00


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.download = 0
        self.upload = 0

    def get_internet_speed(self):
        self.driver.get(URL_OF_SPEEDTEST)
        time.sleep(3)
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()
        time.sleep(60)
        self.upload = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.download = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.driver.close()

    def tweet_at_provider(self):
        self.driver.get(URL_OF_TWITTER)
        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email.send_keys("day_dreamer")
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys("Admin@123")

bot_object = InternetSpeedTwitterBot()
# bot_object.get_internet_speed()
bot_object.tweet_at_provider()
