from selenium.webdriver.common.by import By
from time import sleep

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