from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    mobile_emulation = { "deviceName": "iPhone X" } # Specifying device
    options.add_argument("start-maximized")
    options.add_argument("--auto-open-devtools-for-tabs")
    options.add_experimental_option("mobileEmulation", mobile_emulation) # For mobile emulation
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False) # Disable Chrome Extension
    context.browser = webdriver.Chrome(chrome_options=options)
    # driver.implicitly_wait(10) # 隱性等待，全域影響，最長只等10秒
    context.browser.get("https://www.bob2010.com/entry/login")
    context.wait = WebDriverWait(context.browser, 10)
    
def after_scenario(context, scenario):
    context.browser.quit()