import time
class Loginpageclass():

# declaring locators to the class variables

    textbox_username_id = "username"
    textbox_username_password = "password"
    textbox_username_xpath = "//*[@id='username']"
    textbox_password_xpath = "//*[@id='password']"
    button_login_xpath = "//*[@id='login']/span"

    def __init__(self,driver):
        self.driver=driver


# defining  action for the page objects i.e locators
    def setUsername(self,username):
        time.sleep(2)
        # self.driver.find_element_by_xpath(self.textbox_username_id).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        # self.driver.find_element_by_xpath(self.textbox_username_password).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()




