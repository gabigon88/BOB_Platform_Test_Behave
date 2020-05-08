import pageObject
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep   

options = webdriver.ChromeOptions()
mobile_emulation = { "deviceName": "iPhone X" } # Specifying device
options.add_argument("start-maximized")
options.add_argument("--auto-open-devtools-for-tabs")
options.add_experimental_option("mobileEmulation", mobile_emulation) # For mobile emulation
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False) # Disable Chrome Extension
browser = webdriver.Chrome(chrome_options=options)
# browser.implicitly_wait(10) # 隱性等待，全域影響，最長只等10秒
# browser.get("http://192.168.1.220:3000/entry/login")
# browser.get("http://192.168.1.220:3001/#/entry/login")

# loginPage = pageObject.LoginPage(browser)
# loginPage.InputPhone("15119943624")
# a = loginPage.SendVerification()

browser.get("http://192.168.1.220:3001/#/")
homePage = pageObject.HomePage(browser)
