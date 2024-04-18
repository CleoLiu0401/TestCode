import yaml
from selenium.webdriver.common.by import By
from WebUI.base import BasePage
from WebUI.page.main import MainPage


class Login(BasePage):

    __INPUT_USERNAME = (By.XPATH, "//input[@type='text']")
    __INPUT_PASSWORD = (By.XPATH, "//input[@type='password']")
    __BUTTON_LOGIN = (By.XPATH, "//button[@type='button']")

    def login(self, username, password):

        self.do_send_keys(username, self.__INPUT_USERNAME)
        self.do_send_keys(password, self.__INPUT_PASSWORD)
        self.do_click(self.__BUTTON_LOGIN)

        #获取cookie/token，复用
        cookies=self.driver.get_cookies()
        with open("data.yaml", "w") as f:
            yaml.safe_dump(cookies, f)

        return MainPage(self.driver)
