from WebUI import base as base
from appium.webdriver.common.appiumby import AppiumBy


class MainPage(base):
    __SEARCH = (AppiumBy.ID, "")

    def funa(self):
        self.do_find(*self.__SEARCH)