from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

class Instagrow:

    def __init__(self, driver, username, password):
        self.driver = driver

        # Load instagram site
        self._load_site()
        
        # Log in
        self._log_in(username, password)

    def _log_in(self, username, password):
        in_username = self.driver.find_element_by_name('username')
        in_password = self.driver.find_element_by_name('password')

        # Enter username and password
        in_username.send_keys(username)
        in_password.send_keys(password)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[7]/button').click()
        print('Logged in')
        time.sleep(2)

        # Dismiss any initial popups
        self._dismiss_saveInfo()
        self._dismiss_notifications()
        self._dismiss_homescreen()

    def _load_site(self):
        # Magic strings
        url = 'https://instagram.com/accounts/login'

        # Navigate to Instagram
        self.driver.get(url)
        print('Loaded Instagram')
        time.sleep(2)

    def _dismiss_saveInfo(self):
        # Dismiss notifications popup
        try:
            saveInfo = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/section/div/button')
            saveInfo.click()
            print('Dismissed "Save Your Login Info" popup')
        except:
            print('No "Save Your Login Info" popup')
        time.sleep(2)

    def _dismiss_notifications(self):
        # Dismiss notifications popup
        try:
            pop_notifications = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/button')
            pop_notifications.click()
            print('Dismissed "Show Notifications" popup')
        except:
            print('No "Show Notifications" popup')
        time.sleep(2)

    def _dismiss_homescreen(self):
        # Dismiss homescreen popup
        try:
            pop_homescreen = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
            pop_homescreen.click()
            print('Dismissed "Add to homescreen" popup')
        except:
            print('No "Add to homescreen" popup')
        time.sleep(2)

    def post(self, img):
        # TODO: pass photo to upload
        # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]')
        print('Posted image:', img)

    def follow(self, acc):
        # TODO: Log followed users
        # TODO: Log follow status (i.e. does acc already follow me)
        # TODO: Limit follow frequency, but increase over time (some random, slowly decreasing period between last follow) 
        # TODO: (at usage) Restrict follow probability
        # TODO: (at usage) Determine if target acc is similar in followers and content
        print('Followed', acc)

    def unfollow(self, acc):
        # TODO: (at usage) Determine if an account hasn't followed back in a given window
        # TODO: Log unfollowed acc to prevent autofollow in future
        print('Unfollowed ', acc)

    def like(self, post, acc):
        # TODO: Determine if parameter acc is needed
        # TODO: Don't autolike a photo on a real followee (i.e. an acc that hasn't been autofollowed)
        # TODO: Autolike with same conditions as autofollow, but with increased frequency
        # TODO: (at usage) Primarily autolike photos of potential followers
        print('Liked post', post)

    def comment(self, comment, post, acc):
        # TODO: (at usage) Create a repo of comments
        # TODO: (at usage) Consider determining the sentiment of existing comments
        # TODO: (at usage) Consider determining the relevance of a comment to a photo
        # TODO: Determine if parameters post and acc are needed
        # TODO: Don't autocomment a photo on a real followee
        # TODO: Autolike with same conditions as autolike, but with decreased frequency
        print('Commented "{comment}" on post {post}'.format(comment=comment, post=post))