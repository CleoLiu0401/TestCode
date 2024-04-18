
from appium.webdriver import webdriver

from WeChat.base.base import BasePage
from WeChat.page.mainpage import MainPage


# app相关操作
class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["appPackage"] = ""
            caps["appActivity"] = ""
            caps["deviceName"] = ""
            caps["noReset"] = "true"
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
            #self.driver.start_activity("appPackage", "appActivity")
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_mainpage(self, driver):
        return MainPage(self, driver)
