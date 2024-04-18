import time

import yaml
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from AppUI.base.black import black_wrapper


class BasePage:
    black_list = [(AppiumBy.ID, "")]
    IMPLICITLY_WAIT = 10

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @black_wrapper
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

    def set_implicitly_wait(self, time=10):
        self.driver.implicitly_wait(time)

    def swipe_find(self, text, max_num=3):

        # self.driver.implicitly_wait(1)
        self.set_implicitly_wait()
        """滑动查找一个文本 text
        如果没有找元素，完成滑动操作
        如果找到了，则返回元素
        """
        for num in range(max_num):
            try:
                # find_element() 每次调用这个方法的时候，都会激活隐式等待，也就是在隐式等待的时长之内，动态的找元素
                element = self.driver.find_element(AppiumBy.XPATH, f"//*[@text='{text}']")
                # 找到了元素之后，再设置回全局的隐式等待时长 10秒
                # self.driver.implicitly_wait(self.IMPLICITLY_WAIT)
                self.set_implicitly_wait(self.IMPLICITLY_WAIT)
                return element
            except NoSuchElementException as e:
                print("未找到元素")
                # 滑动 从下向上
                size = self.driver.get_window_size()
                # 'width', 'height'
                width = size.get("width")
                height = size.get("height")

                startx = width / 2
                starty = height * 0.8

                endx = startx
                endy = height * 0.2

                duration = 2000
                self.driver.swipe(startx, starty, endx, endy, duration)

            if num == max_num - 1:
                # 没有找到的情况。在抛出异常之前，把这个隐式等待改回全局的等待时长 10秒
                # self.driver.implicitly_wait(self.IMPLICITLY_WAIT)
                self.set_implicitly_wait(self.IMPLICITLY_WAIT)
                # 执行到最大次数，仍然没有找到这个文本，则抛出异常
                raise NoSuchElementException(f"找了{num} 次，未找到{text}")


class Test:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = ""
        caps["appActivity"] = ""
        caps["deviceName"] = ""
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("url", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()







