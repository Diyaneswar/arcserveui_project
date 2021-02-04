import time
class Addsrc_pageobjects:

    def __init__(self, driver):
        self.driver = driver

    btn_protect_xpath = r'//body/div[@id="root"]/div[1]/div[1]/div[1]/ul[1]/li[3]'
    def btn_protect_menu(self):
        self.driver.find_element_by_xpath(self.btn_protect_xpath).click()

    btn_addsrc_xpath = r"//body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/button[1]/span[1]"
    def btn_addsrc_menu(self):
        self.driver.find_element_by_xpath(self.btn_addsrc_xpath).click()

    btn_addwin_xpath = r"//span[contains(text(),'Add Windows Source')]"
    def drp_addwin(self):
        self.driver.find_element_by_xpath(self.btn_addwin_xpath).click()

    btn_site_xpath = r"//*[@id='recipientMailReportModal']/div/div/button"
    def btn_selsite(self):
        self.driver.find_element_by_xpath(self.btn_site_xpath).click()

    drp_site_xpath=r"//body[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[5]/span[1]"
    def drp_hpsite(self):
        self.driver.find_element_by_xpath(self.drp_site_xpath).click()

    txt_srcname_xpath = r"//input[@name='sourceName']"
    txt_usrname_xpath = r"//input[@name='userName']"
    txt_psswd_xpath = r"//input[@name='password']"
    btn_save_xpath = r"//*[@id='create-course-form']/div/div[1]/button"

    def txt_srcname(self, srcname):
        self.driver.find_element_by_xpath(self.txt_srcname_xpath).send_keys(srcname)

    def txt_usrname(self, username):
        self.driver.find_element_by_xpath(self.txt_usrname_xpath).send_keys(username)

    def txt_pwd(self, password):
        self.driver.find_element_by_xpath(self.txt_psswd_xpath).send_keys(password)

    def btn_addwin(self):
        self.driver.find_element_by_xpath(self.btn_save_xpath).click()

    btn_addsrc_xpath = r"/html/body/div[3]/div/div/div[2]/form/div[2]/div[2]/button[2]/span"
    def btn_addsrc(self):
        self.driver.find_element_by_xpath(self.btn_addsrc_xpath).click()