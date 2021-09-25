from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options

import time

class BrowserController:
    def __init__(self):
        pass
    def open(self, url):
        options = Options()
        options.add_argument("--disable-notifications")
        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.get(url)
        time.sleep(1)

    def login(self, **kwargs):
        input_account = self.browser.find_element_by_id(kwargs["input_account_id"])
        input_password = self.browser.find_element_by_id(kwargs["input_password_id"])
        btn_login = self.browser.find_element_by_id(kwargs["button_login_id"])

        input_account.clear()
        input_account.send_keys(kwargs["account"])
        input_password.clear()
        input_password.send_keys(kwargs["password"])
        time.sleep(0.5)

        btn_login.click()

    def reload(self):
        self.browser.execute_script("setTimeout(()=>{window.location.reload();}, 0)")
    
    def close(self):
        self.browser.quit()
