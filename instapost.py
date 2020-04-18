from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep
from pathlib import Path

class Instapost:

    def __init__(self, driver, email, password):
        self.driver = driver
        self._load_site()
        
        # Log in with insta
        btn_login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]/div[2]/div/div[1]/div[2]/button')
        btn_login.click()
        
        # Switch to new login window
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        # Enter username and password
        in_email = self.driver.find_element_by_name('email')
        in_password = self.driver.find_element_by_name('pass')

        in_email.send_keys(email)
        in_password.send_keys(password)

        # Submit login details
        self.driver.find_element_by_name('login').click()

    def _load_site(self):
        # Load Creator Studio
        url = 'https://business.facebook.com/creatorstudio'
        self.driver.get(url)
        sleep(3)