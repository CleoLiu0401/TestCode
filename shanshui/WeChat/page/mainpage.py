from selenium.webdriver.common.by import By

from WebUI.base.base import BasePage
from WebUI.page.courses import Courses


class MainPage(BasePage):

    _BASE_URL = "https://www.shanshui65.net/"
    #menu
    __MENU_MAINPAGE = (By.CSS_SELECTOR, "n-button n-button--primary-type n-button--medium-type")
    __MENU_COURSES = (By.CSS_SELECTOR, ".n-submenu:nth-child(2) > .n-submenu-children > .n-menu-item:nth-child(1) .n-menu-item-content-header")
    __MENU_CART = (By.CSS_SELECTOR, ".n-submenu:nth-child(2) .n-menu-item:nth-child(2) .n-menu-item-content-header")
    __MENU_CENTER = (By.CSS_SELECTOR, ".n-submenu:nth-child(5) .n-menu-item-content-header")

    def goto_mainpage(self):
        self.do_click(self.__MENU_MAINPAGE)
        return MainPage(self.driver)

    def goto_courses(self):
        self.do_click(self.__MENU_COURSES)
        return Courses(self.driver)

    def goto_cart(self):
        self.do_click(self.__MENU_CART)
        return Cart(self.driver)

    def goto_center(self):
        self.do_click(self.__MENU_CENTER)

