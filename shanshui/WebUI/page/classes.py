from selenium.webdriver.common.by import By

from WebUI.base.base import BasePage


class Classes(BasePage):
    __LIST_CLASS_NAME = (By.XPATH, "//button[@type='button']")
    __BUTTON_ADD = (By.CSS_SELECTOR, ".n-button__content > .inline-block")
    __BUTTON_SAVE = (By.XPATH, "//button[contains(.,'确认')]")

    def get_classes(self, class_name):
        class_name = self.do_find(By.XPATH, "//td[contains(.,'" + class_name + "')]")
        return class_name

    def add_class(self, class_name):
        # 添加按钮
        self.do_click(self.__BUTTON_ADD)
        # 课程分组
        self.do_click(By.XPATH, "//form/div/div/div/div/div/div/div")
        self.do_click(By.XPATH, "//div[2]/div/span[2]")
        # 课程名称
        self.do_click(By.XPATH, "//form/div/div[2]/div/div/div/div/div")
        self.do_click(By.CSS_SELECTOR, ".n-base-select-option--pending")
        # 班级名称
        self.do_send_keys(class_name, By.XPATH, "(//input[@type='text'])[2]")
        # 班级容量
        self.do_send_keys("45", By.XPATH, "(//input[@type='text'])[5]")
        # 首席班主任
        self.do_click(By.XPATH, "//div[7]/div/div/div/div/div")
        self.do_click(By.CSS_SELECTOR, ".v-binder-follower-container:nth-child(4) .n-base-select-option")
        # 督导老师
        self.do_click(By.XPATH, "//div[9]/div/div/div/div/div")
        self.do_click(By.CSS_SELECTOR, ".v-binder-follower-container:nth-child(5) .n-base-select-option__content")
        # 主讲老师
        self.do_click(By.XPATH, "//div[10]/div/div/div/div/div")
        self.do_click(By.CSS_SELECTOR, ".v-binder-follower-container:nth-child(6) .n-base-select-option__content")
        # 首席助教老师
        self.do_click(By.XPATH, "//div[11]/div/div/div/div/div")
        self.do_click(By.CSS_SELECTOR, ".v-binder-follower-container:nth-child(7) .n-base-select-option__content")
        # 销售状态
        self.do_send_keys("13", By.XPATH, "(//input[@type='text'])[6]")
        self.do_send_keys("28", By.XPATH, "(//input[@type='text'])[7]")
        self.do_send_keys("28", By.XPATH, "(//input[@type='text'])[8]")
        self.do_send_keys("32", By.XPATH, "(//input[@type='text'])[9]")
        self.do_send_keys("32", By.XPATH, "(//input[@type='text'])[10]")
        # 保存
        self.do_click(self.__BUTTON_SAVE)

        self.get_screenshot()

        return Classes()
