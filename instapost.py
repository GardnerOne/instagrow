from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep
from pathlib import Path

class Instapost:

    def __init__(self, driver, email, password):
        self.driver = driver
        self.actions = ActionChains(self.driver)

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

        # Switch to Instagram Creator Studio
        btn_insta = self.driver.find_element_by_xpath('//*[@id="media_manager_chrome_bar_instagram_icon"]')
        btn_insta.click()
        sleep(3)

    def _load_site(self):
        # Load Creator Studio
        url = 'https://business.facebook.com/creatorstudio'
        self.driver.get(url)
        sleep(2)

    def createPost(self, caption, post):
        # Click on create post button
        self.driver.find_element_by_xpath('//*[@id="mediaManagerLeftNavigation"]/div[1]/div/a').click()
        sleep(1)
        # TODO: expand to add IGTV
        # Choose instagram feed
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div/ul/li[1]').click()
        sleep(2)

        # Add a caption with hashtags
        # TODO: add @mentions with other accounts
        # TODO: create a bank of auto-hashtags (max 30 in one go)
        hashtags = '#portraitsquad #portraitvision #portraitsfromtheworld #collectivetrend #canonportraits #dreamportraits #portraitphotography #canonlglass #canon70d'
        caption = caption + '\n.\n.\n.\n' + hashtags
        caption.replace('\n', Keys.ENTER)
        
        txt_placeholder = self.driver.find_element_by_xpath('//*[@id="creator_studio_sliding_tray_root"]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/div/div/span/br')
        txt_placeholder.find_element_by_xpath('../..').click()

        # Add caption
        self.actions.send_keys(caption)
        self.actions.perform()

        btn_addContent = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/div[1]/div/div[5]/div/div/div')
        btn_addContent.click()

        # Add post
        str_home = str(Path.home())
        str_folder = '/Pictures/instagram/'
        in_post = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div/div/a/div/input')
        in_post.send_keys(str_home + str_folder + post)

        # Publish
        # TODO: schedule
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/div[2]/button').click()

