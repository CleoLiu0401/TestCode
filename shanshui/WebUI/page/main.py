from selenium.webdriver.common.by import By

from WebUI.base.base import BasePage
from WebUI.page.activities import Activities
from WebUI.page.classes import Classes
from WebUI.page.courses import Courses


class MainPage(BasePage):

    # _BASE_URL = "https://www.shanshui65.net/"
    #menu div.n-submenu:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)
    __MENU_EDU = (By.CSS_SELECTOR, ".n-submenu:nth-child(2) .n-menu-item-content-header")
    __MENU_EDU_COURSES = (By.CSS_SELECTOR, ".n-submenu:nth-child(2) > .n-submenu-children > .n-menu-item:nth-child(1) .n-menu-item-content-header")
    __MENU_EDU_CLASS = (By.CSS_SELECTOR, ".n-submenu:nth-child(2) > .n-submenu-children > .n-menu-item:nth-child(2) .n-menu-item-content-header")
    __MENU_ACTI = (By.CSS_SELECTOR, ".n-submenu:nth-child(5) .n-menu-item-content-header")
    __MENU_ACTI_DISCOUNT = (By.CSS_SELECTOR, ".n-submenu:nth-child(5) .n-menu-item:nth-child(2) .n-menu-item-content-header")

    def goto_courses(self):
        self.do_click(self.__MENU_EDU)
        self.do_click(self.__MENU_EDU_COURSES)
        return Courses(self.driver)

    def goto_classes(self):
        self.do_click(self.__MENU_EDU)
        self.do_click(self.__MENU_EDU_CLASS)
        return Classes(self.driver)

    def goto_activities(self):
        self.do_click(self.__MENU_ACTI)
        self.do_click(self.__MENU_ACTI_DISCOUNT)
        return Activities(self.driver)

