from selenium.webdriver.common.by import By

from WebUI.base.base import BasePage


class Activities(BasePage):

    __BUTTON_ADD = (By.XPATH, "//button[contains(.,'新增')]")
    __BUTTON_SAVE = (By.XPATH, "//button[contains(.,'保存')]")

    def get_activities(self, activity_name):
        activity_name = self.do_find(By.XPATH, "//td[contains(.,'" + activity_name + "')]")
        return activity_name

    def add_activity(self, activity_name, start_time, end_time):
        # 添加按钮
        self.do_click(self.__BUTTON_ADD)
        # 活动名称
        self.do_send_keys(activity_name, By.XPATH, "//input[@type='text']")
        # 活动时间
        self.do_send_keys(start_time, By.XPATH, "(//input[@type='text'])[2]")
        self.do_send_keys(end_time, By.XPATH, "(//input[@type='text'])[3]")
        # 选择课程
        self.do_click(By.XPATH, "//span[contains(.,'选择课程')]")
        self.do_click(By.CSS_SELECTOR, ".n-tree-node-wrapper:nth-child(2) .n-tree-node-content__text")
        self.do_click(By.CSS_SELECTOR, "//td/label/input")
        self.do_click(By.XPATH, "//button[contains(.,'确定')]")
        # 保存
        self.do_click(self.__BUTTON_SAVE)

        self.get_screenshot()

        return Activities()
