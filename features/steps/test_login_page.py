from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

# given-----------------------------------------------
@given('I open login page')
def step_impl(context):
    pass


# when-----------------------------------------------
@when('I input {account} in account field')
def step_impl(context, account):
    accountTF_XPath = '//*[@id="app"]//input[@placeholder="请输入用户名"]'
    accountTF = context.wait.until(EC.visibility_of_element_located((By.XPATH, accountTF_XPath)))
    accountTF.clear()
    accountTF.send_keys(account)

@when('I input {password} in password field')
def step_impl(context, password):
    passwordTF_XPath = '//*[@id="app"]//input[@placeholder="请输入密码"]'
    passwordTF = context.wait.until(EC.visibility_of_element_located((By.XPATH, passwordTF_XPath)))
    passwordTF.clear()
    passwordTF.send_keys(password)

@when('I click login page button')
def step_impl(context):
    loginPageBtn_XPath = '//*[@id="app"]//div[@class="_2jL7LBfB"]/div[contains(text(), "登录")]'
    loginPageBtn = context.wait.until(EC.visibility_of_element_located((By.XPATH, loginPageBtn_XPath)))
    loginPageBtn.click()

@when('I click register page button')
def step_impl(context):
    registerPageBtn_XPath = '//*[@id="app"]//div[@class="_2jL7LBfB"]/div[contains(text(), "注册")]'
    registerPageBtn = context.wait.until(EC.visibility_of_element_located((By.XPATH, registerPageBtn_XPath)))
    registerPageBtn.click()

@when('I click show password button')
def step_impl(context):
    showPasswordBtn_XPath = '//*[@id="app"]//i'
    showPasswordBtn = context.wait.until(EC.visibility_of_element_located((By.XPATH, showPasswordBtn_XPath)))
    showPasswordBtn.click()

@when('I click forgot password')
def step_impl(context):
    link_XPath = '//*[@id="app"]//div[@class="yfR7rih-"]'
    link = context.wait.until(EC.visibility_of_element_located((By.XPATH, link_XPath)))
    link.click()

@when('I click login button')
def step_impl(context):
    btn_XPath = '//*[@id="app"]//div[@class="_4Qzzl4Bo"]'
    btn = context.wait.until(EC.visibility_of_element_located((By.XPATH, btn_XPath)))
    btn.click()

@when('I click {link_text} link')
def step_impl(context, link_text):
    link_XPath = f'//p[contains(text(), "{link_text}")]'
    link = context.wait.until(EC.visibility_of_element_located((By.XPATH, link_XPath)))
    sleep(1) # wait到element之後如果馬上click會開啟空白的新分頁，推測是JS還沒執行完畢
    link.click()


# then-----------------------------------------------
@then('the {password} is visible')
def step_impl(context, password):
    passwordTF_XPath = '//*[@id="app"]//input[@placeholder="请输入密码"]'
    passwordTF = context.wait.until(EC.visibility_of_element_located((By.XPATH, passwordTF_XPath)))
    assert password.lower() == passwordTF.get_attribute("value")

@then('page is login page')
def step_impl(context):
    assert context.browser.current_url == "https://www.bob2010.com/entry/login"

@then('page is register page')
def step_impl(context):
    assert context.browser.current_url == "https://www.bob2010.com/entry/register"

@then('page is forgot password page')
def step_impl(context):
    assert "https://www.bob2010.com/app/findPassword" in context.browser.current_url

@then('open new window of {page_url_tag}')
def step_impl(context, page_url_tag):
    context.browser.switch_to.window(context.browser.window_handles[1])
    sleep(1) # 新分頁有跳轉的動作，要等待跳轉完畢才獲取url
    assert page_url_tag in context.browser.current_url

@then('home page userName is {account}')
def step_impl(context, account):
    userName_XPath = '//div[@class="_20lF07A5"]/span'
    userName = context.wait.until(EC.visibility_of_element_located((By.XPATH, userName_XPath)))
    assert context.browser.current_url == 'https://www.bob2010.com/app/home'
    assert userName.text == account

