import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _BASE_URL = ""

    def __init__(self, base_driver=None):
        if base_driver:
            self.driver = base_driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()

        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL)

    def do_find(self, by, locator=None):
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def do_finds(self, by, locator=None):
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, value, by, locator=None):
        ele = self.do_find(by, locator)
        ele.clear()
        ele.send_keys(value)

    def do_click(self, by, locator=None):
        button = self.do_find(by, locator)
        button.click()

    def do_quit(self):
        self.driver.quit()

    def get_screen(self):
        timestamp = int(time.time())
        image_path = f"./images/image_{timestamp}.PNG"
        # 截图
        self.driver.save_screenshot(image_path)
        # 将截图放到报告的数据中
        allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)

    def wait_element_visible(self, locator: tuple):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def get_cookies(self):
        cookies = yaml.safe_load(open("../data.yaml"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)




