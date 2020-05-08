from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

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

class LoginPage(BasePage):
    __loginBtn_loc = (By.XPATH, '//span[contains(text(), "登录")] | //span[contains(text(), "登入")]')
    __accountTF_loc = (By.XPATH, '//input[@placeholder="请输入手机号码"] | //input[@placeholder="請輸入手機號碼"]')
    __passwordTF_loc = (By.XPATH, '//input[@placeholder="請輸入驗證碼"] | //input[@placeholder="请输入验证码"]')
    __verificationTF_loc = (By.XPATH, '//input[@class="MuiInputBase-input MuiInput-input Mui-disabled Mui-disabled MuiInputBase-inputAdornedStart MuiInputBase-inputAdornedEnd"]')
    __sendVerificationBtn_loc = (By.XPATH, '//span[contains(text(), "发送验证码")]/.. | //span[contains(text(), "發送驗證碼")]/..')
    __getVerificationBtn_loc = (By.XPATH, '//span[contains(text(), "取得验证码")]/..')
    __goToLoginBtn_loc = (By.XPATH, '//div[contains(text(), "登录")] | //div[contains(text(), "登錄")]')
    __goToRegisterBtn_loc = (By.XPATH, '//div[contains(text(), "注册")] | //div[contains(text(), "註冊")]')

    def __init__(self, _driver):
        super(LoginPage, self).__init__(_driver)
    
    def InputPhone(self, account):
        self.find_element(*self.__accountTF_loc).clear()
        self.find_element(*self.__accountTF_loc).send_keys(account)

    def InputVerification(self, password):
        self.find_element(*self.__passwordTF_loc).clear()
        self.find_element(*self.__passwordTF_loc).send_keys(password)

    def GetAccount(self):
        return self.find_element(*self.__accountTF_loc).text

    def GetPassword(self):
        return self.find_element(*self.__passwordTF_loc).text

    def SendVerification(self):
        self.driver.find_element(*self.__sendVerificationBtn_loc).click()
        self.waitForAlert()
        self.driver.find_element(*self.__getVerificationBtn_loc).click()
        return self.driver.find_element(*self.__verificationTF_loc).text
        
    def GoToLoginPage(self):
        self.driver.find_element(*self.__goToLoginBtn_loc).click()
        sleep(1)

    def GoToRegisterPage(self):
        self.driver.find_element(*self.__goToRegisterBtn_loc).click()
        sleep(1)

    def Login(self, account=None, password=None):
        if account is not None:
            self.InputPhone(account)
        if password is not None:
            self.InputVerification(password)
        self.wait.until(EC.visibility_of_element_located(self.__loginBtn_loc))
        self.find_element(*self.__loginBtn_loc).click()
        self.waitForAlert()

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