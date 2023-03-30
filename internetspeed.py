from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
import os

CHROME_PATH = r"C:\Users\user\OneDrive - Whitireia and WelTec\Desktop\Bianca\IT\Web Development\chromedriver.exe"
TWITTER_EMAIL = "biancafiedalan31@yahoo.com"

class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(CHROME_PATH), options=self.chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)
        self.go_btn = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        self.go_btn.click()

        time.sleep(40)
        dl_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
        up_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.down = float(dl_speed.text)
        self.up = float(up_speed.text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")

        log_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a/div/span/span')
        log_in.click()

        time.sleep(3)
        username = self.driver.find_element(By.TAG_NAME, 'input')
        username.send_keys("acabianca666")
        username.send_keys(Keys.RETURN)
        time.sleep(3)

        pw = self.driver.find_element(By.NAME, 'password')
        pw.send_keys(os.environ.get("PASSWORD"))
        pw.send_keys(Keys.RETURN)

        time.sleep(7)
        type_msg = self.driver.find_element(By.CSS_SELECTOR, '.DraftEditor-editorContainer div')
        type_msg.click()
        type_msg.send_keys("MY FIRST TWITTER BOT LETS GOOOOOOOOOOOOOO!!")
        type_msg.send_keys(Keys.RETURN)

        time.sleep(5)
        tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.click()

        time.sleep(10)
        self.driver.quit()


