import yaml
from selenium.webdriver.common.by import By

from WebUI.base import BasePage
from Interface.utils.log_util import logger


class Login(BasePage):

    _BASE_URL = "url"
    __INPUT_USERNAME = (By.NAME, "username")
    __INPUT_PASSWORD = (By.NAME, "password")
    __BUTTON_LOGIN = (By.CSS_SELECTOR, "el-button--primary")

    def login(self):
        logger.info("访问登录页")

        self.do_send_keys("manege",self.__INPUT_USERNAME)
        self.do_send_keys("manege123", self.__INPUT_PASSWORD)
        self.do_click(self.__BUTTON_LOGIN)

        #获取cookie/token，复用
        cookies=self.driver.get_cookies()
        with open("cookie.yaml","w") as f:
            yaml.safe_dump(cookies,f)
        #token = self.driver.execute_script('return sessionStorage.getItem("token");')
        # cookie = yaml.safe_load(open("cookie.yaml"))
        # for c in cookie:
        #     self.driver.add_cookie(c)

        # return NextPage(self.driver)
