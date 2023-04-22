from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH =  YOUR CHROMEDRIVER PATH
instagram_EMAIL = YOUR INSTAGRAM USERNAME
instagram_PASSWORD = YOUR INSTAGRAM PASSWORD
account_to_follow = INSTA ACCOUNT WHOS FOLLOWERS YOU WANT TO FOLLOW


class Instafollower():
    def __init__(self, driver_path):
        self.opt = Options()
        self.opt.headless = True
        self.chrome_driver_path = CHROME_DRIVER_PATH
        self.ser = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.ser)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(instagram_EMAIL)
        password.send_keys(instagram_PASSWORD)
        time.sleep(2)

        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        time.sleep(5)

        login_notification = self.driver.find_element(By.CSS_SELECTOR, '.xwhw2v2')
        login_notification.click()
        time.sleep(2)

        turn_notification = self.driver.find_element(By.CSS_SELECTOR, '._a9-z button')
        turn_notification.click()

        time.sleep(2)

    def find_follower(self):
        self.driver.get(f"https://www.instagram.com/{account_to_follow}/followers/")
        time.sleep(5)

    def follow(self, times_click=10):

        f_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div._aano button._acan._acap._acas._aj1-')
        try:
            for i in range(times_click):
                button = f_buttons[i]
                button.click()
                time.sleep(3)
                print("Followed")
        except ElementClickInterceptedException:  # click cancel if already following
            cancel = self.driver.find_element(By.CSS_SELECTOR, 'button._a9--._a9_1')
            cancel.click()
            print("skipped")
            time.sleep(2)


bot = Instafollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_follower()
bot.follow()
