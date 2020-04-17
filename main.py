from instagrow import Instagrow
from utilities.secrets import pwd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Launch mobile emulator browser
chromedriver = '/Users/gardnerone/dev/utilities/chromedriver'
service = Service(chromedriver)
service.start()
print('ChromeDriver started')

mobile_emulation = { "deviceName": "iPhone X" }

options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Remote(
    command_executor=service.service_url,
    desired_capabilities = options.to_capabilities())
print('Mobile Emulation started')

# Open account with Instagrow
username = 'gardner.one'
instagrow = Instagrow(driver, username, pwd)

print('Interactive mode started')