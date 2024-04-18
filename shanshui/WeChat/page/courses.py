from selenium.webdriver.common.by import By

from WebUI.base.base import BasePage


class Courses(BasePage):
    __BUTTON_ADD = (By.CCS_SELECTOR, ".n-button--primary-type > .n-button__content")
    __BUTTON_SAVE = (By.XPATH, "//span[contains(.,'保存')]")
    __COURSE_GROUP = (By.XPATH, "//main[@id='__SCROLL_EL_ID__']/div/div/div/form/div/div[2]/div/div/div/div/div")
    __COURSE_SEASON = (By.XPATH, "//main[@id='__SCROLL_EL_ID__']/div/div/div/form/div/div[3]/div/div/div/div/div")
    __COURSE_NAME = (By.XPATH, "//main[@id='__SCROLL_EL_ID__']/div/div/div/form/div/div[4]/div/div/div/div/div/input")

    def get_courses(self, course_name):
        course = self.do_find(By.XPATH, "//td[contains(.,'" + course_name + "')]")
        return course

    def add_course(self, course_name):
        # 添加按钮
        self.do_click(self.__BUTTON_ADD)
        # 课程分组
        self.do_click(self.__COURSE_GROUP)
        self.do_click(By.CCS_SELECTOR, ".n-tree-node-switcher__icon svg")
        self.do_click(By.CCS_SELECTOR, ".n-tree-node-wrapper:nth-child(2) .n-tree-node-content__text")
        # 课程时节
        self.do_click(self.__COURSE_SEASON)
        self.do_click(By.CCS_SELECTOR, ".n-base-select-option--pending")
        # 课程名称
        self.do_send_keys(course_name, self.__COURSE_NAME)
        # 授课方式
        self.do_click(By.XPATH, "//main[@id='__SCROLL_EL_ID__']/div/div/div/form/div/div[5]/div/div/div/div/div")
        self.do_click(By.XPATH, "//body/div[6]/div/div/div/div/div/div/div/div")
        # 班级规模
        self.do_click(By.XPATH, "//main[@id='__SCROLL_EL_ID__']/div/div/div/form/div/div[6]/div/div/div/div/div")
        self.do_click(By.XPATH, "//body/div[7]/div/div/div/div/div/div/div")
        # 课程内容
        self.do_click(By.XPATH, "//main[@id='__SCROLL_EL_ID__']/div/div/div/form/div/div[7]/div/div/div/div/div")
        self.do_click(By.XPATH, "//div[8]/div/div/div/div/div/div/div[2]/div")
        # 课程等级
        self.do_click(By.XPATH, "//main[@id='__SCROLL_EL_ID__']/div/div/div/form/div/div[8]/div/div/div/div/div")
        self.do_click(By.XPATH, "//div[9]/div/div/div/div/div/div/div/div")
        # 课程主题
        self.do_click(By.XPATH, "//main[@id='__SCROLL_EL_ID__']/div/div/div/form/div/div[9]/div/div/div/div/div")
        self.do_click(By.XPATH, "//div[10]/div/div/div/div/div/div/div/div")
        # 适合年级
        self.do_click(By.XPATH, "//main[@id='__SCROLL_EL_ID__']/div/div/div/form/div/div[10]/div/div/div/div/div")
        self.do_click(By.XPATH, "//div[11]/div/div/div/div/div/div/div/div")
        # 课程封面
        self.do_click(By.XPATH, "//span[contains(.,'选择封面')]")
        self.do_click(By.CCS_SELECTOR, ".n-radio-input")
        self.do_click(By.XPATH, "//button[contains(.,'确定')]")
        # 课程视频
        self.do_click(By.XPATH, "//span[contains(.,'选择视频')]")
        self.do_click(By.XPATH, "//div[4]/div[2]/span")  # 视频tab
        self.do_click(By.CCS_SELECTOR, ".n-tree-node-wrapper:nth-child(3) .n-tree-node-content__text")  # 树
        self.do_click(By.CCS_SELECTOR, ".n-radio-input")
        self.do_click(By.XPATH, "//span[contains(.,'确定')]")
        # 课程简介
        self.do_send_keys("UI自动化测试", By.XPATH,
                          "//main[@id='__SCROLL_EL_ID__']/div/div/div/form/div/div[16]/div/div/div/div/div/textarea")
        # 课程大纲
        self.do_send_keys("第一讲", By.XPATH,
                          "//main[@id='__SCROLL_EL_ID__']/div/div/div/form/div/div[17]/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr/td/div/div/div/input")
        self.do_send_keys("使者", By.XPATH,
                          "//main[@id='__SCROLL_EL_ID__']/div/div/div/form/div/div[17]/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]/div/div/div/input")
        # 课程详情
        self.do_click(By.XPATH, "//span[contains(.,'选择详情')]")
        self.do_click(By.XPATH, "//label/input")
        self.do_click(By.XPATH, "//button[contains(.,'确定')]")
        # 购买需知
        self.do_click(By.XPATH, "//span[contains(.,'选择须知')]")
        self.do_click(By.XPATH, "//label/input")
        self.do_click(By.XPATH, "//span[contains(.,'确定')]")
        # 课程价格
        self.do_send_keys("2499", By.XPATH,
                          "//main[@id='__SCROLL_EL_ID__']/div/div/div/form/div/div[21]/div/div/div/div/div/div/input")
        # 勾选教材邮寄
        self.do_click(By.CCS_SELECTOR, "div:nth-child(23) .n-checkbox-box__border")
        # 勾选积分抵现
        self.do_click(By.CCS_SELECTOR, "div:nth-child(25) .n-checkbox-box__border")
        # 保存
        self.do_click(self.__BUTTON_SAVE)

        self.get_screenshot()

        return Courses()
