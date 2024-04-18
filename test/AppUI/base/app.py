from WebUI import base as base
from appium.webdriver import webdriver


# app相关操作
class App(base):
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["appPackage"] = ""
            caps["appActivity"] = ""
            caps["deviceName"] = ""
            caps["noReset"] = "true"
            self.driver = webdriver.Remote("url", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self, driver):
        from AppUI.page.MainPage import MainPage

        return MainPage(self, driver)