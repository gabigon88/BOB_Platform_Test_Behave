from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self, _driver):
        self.driver = _driver
        self.wait = WebDriverWait(_driver, 10)
    
    def close(self):
        self.driver.close()

    def find_element(self, *loc):
        return self.wait.until(EC.visibility_of_element_located(loc))

    def find_elements(self, *loc):
        self.wait.until(EC.visibility_of_element_located(loc))
        return self.driver.find_elements(*loc)

    def waitForAlert(self):
        try:
            alert = self.driver.find_element(By.XPATH, '//*[@role="alert"]')
            self.wait.until(EC.staleness_of(alert))
        except:
            pass