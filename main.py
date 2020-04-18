from instagrow import Instagrow
from instapost import Instapost
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import utilities.secrets as secret

# # Launch mobile emulator browser
# chromedriver = '/Users/gardnerone/dev/utilities/chromedriver'
# service = Service(chromedriver)
# service.start()
# print('ChromeDriver started')

# mobile_emulation = { "deviceName": "iPhone X" }

# options = webdriver.ChromeOptions()
# options.add_experimental_option("mobileEmulation", mobile_emulation)
# driver = webdriver.Remote(
#     command_executor=service.service_url,
#     desired_capabilities = options.to_capabilities())
# print('Mobile Emulation started')

# # Open account with Instagrow
# username = 'gardner.one'
# instagrow = Instagrow(driver, username, pwd)

chromedriver = '/Users/gardnerone/dev/utilities/chromedriver'
driver = webdriver.Chrome(chromedriver)

email = 'jamiedanielgardner@outlook.com'
instapost = Instapost(driver, email, secret.pwd_fb)

# TODO: create a bank of auto-captions
caption = 'Who do you see when you look in the mirror?\n\n\nWith @complaineee (also on TikTok!)'
post = 'insta-1.jpg'
instapost.createPost(caption, post)

print('Interactive mode started')