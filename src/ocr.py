class JSOCR:
    def __init__(self, js_path: str):
        self.js_path = js_path
    def recognize_captcha_on_browser(self, browser):
        js = ""
        with open(self.js_path, "r") as f:
            js = f.read()
        return browser.execute_async_script(js)