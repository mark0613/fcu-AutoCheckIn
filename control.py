import time
import os
from datetime import datetime, timedelta
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

from src.load import load_json
from src.ocr import JSOCR
from src.browser import BrowserController
from src.time_extension import time_compare, time_delta

WEEK = {
    "0" : "Mon",
    "1" : "Tue",
    "2" : "Wed",
    "3" : "Thu",
    "4" : "Fri",
    "5" : "Sat",
    "6" : "Sun",
}
TIME = {
    "01" : "08:10",
    "02" : "09:10",
    "03" : "10:10",
    "04" : "11:10",
    "05" : "12:10",
    "06" : "13:10",
    "07" : "14:10",
    "08" : "15:10",
    "09" : "16:10",
    "10" : "17:10",
    "11" : "18:30",
    "12" : "19:25",
    "13" : "20:25",
    "14" : "21:20",
}
URL = "https://signin.fcu.edu.tw/clockin/login.aspx"

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

class AutoCheckIn:
    def __init__(self):
        self.class_time = load_json(f"{CURRENT_PATH}/data/class_time.json")

        self.browser = BrowserController()
        self.browser.open(URL)
        self.chrome = self.browser.browser      

    def recognize_captcha(self):
        return JSOCR(f"{CURRENT_PATH}/src/captcha.js").recognize_captcha_on_browser(self.chrome)

    def login(self, account, password):
        self.browser.login(
            input_account_id = "LoginLdap_UserName",
            input_password_id = "LoginLdap_Password",
            button_login_id = "LoginLdap_LoginButton",
            account = account,
            password = password,
        )
        self.chrome.find_element_by_id("ButtonClassClockin").click()

    def reload(self):
        self.browser.reload()

    def check_in(self):
        while True:
            try:
                input_captcha = self.chrome.find_element_by_id("validateCode")
                btn_signin = self.chrome.find_element_by_id("Button0")

                input_captcha.clear()
                input_captcha.send_keys(self.recognize_captcha())
                time.sleep(0.5)
                btn_signin.click()
            except NoSuchElementException:
                return
            except ElementClickInterceptedException:
                return

    def execute(self):
        def is_valid_time(class_time: str, now_time: str):
            c_t = datetime.strptime(class_time, "%H:%M") + timedelta(minutes=48)
            n_t = datetime.strptime(now_time, "%H:%M")
            return c_t >= n_t
        
        now_week = WEEK[str(time.localtime().tm_wday)]
        today_class = [TIME[i] for i in self.class_time[now_week] if self.class_time[now_week][i]==True]
        now_time = f"{time.localtime().tm_hour}:{time.localtime().tm_min}"

        valid_time = []
        for t in today_class:
            if is_valid_time(t, now_time):
                valid_time.append(t)

        while len(valid_time) > 0:
            now_time = f"{time.localtime().tm_hour}:{time.localtime().tm_min}"
            if time_compare(now_time, valid_time[0], "%H:%M"):
                self.check_in()
                valid_time.pop(0)
            if len(valid_time) == 0: break
            time.sleep(60)
            self.reload()
        self.browser.close()


if __name__ == "__main__":
    print("Please Execute autoCheckInMain.py")


