from selenium.webdriver.common.by import By
from time import sleep

class HomePage(BasePage):
    __alertBtn_loc = (By.XPATH, '//span[@class="MuiButton-label"]')

    def __init__(self, _driver):
        super(HomePage, self).__init__(_driver)
        self.driver.find_element(*self.__alertBtn_loc).click()
    
    def ClickTagOf(self, tag):
        self.driver.find_element(By.XPATH, f'//*[contains(text(), "{tag}")]/..').click()

    def GoToDepositsPage(self):
        self.ClickTagOf('存款')
    
    def GoToWithdrawalPage(self):
        self.ClickTagOf('取款')

    def GoToVipPage(self):
        self.ClickTagOf('VIP详情')
    
    def GoToPromoPage(self):
        self.ClickTagOf('优惠')
    
    def GoToSupportPage(self):
        self.ClickTagOf('客服')

    def GoToHomePage(self):
        self.ClickTagOf('首页')
        self.driver.find_element(*self.__alertBtn_loc).click()

    def GoToSponsorPage(self):
        self.ClickTagOf('赞助')

    def GoToMemberPage(self):
        self.ClickTagOf('我的')