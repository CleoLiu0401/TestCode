from WeChat.page.applet import App


class TestCase:
    def setup_class(self):
        pass

    def teardown_class(self):
        self.home.do_quit()

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_mainpage()

    @pytest.mark.parametrize("course_name", "l课程")  # 参数化
    def test_add_course(self, course_name):
        #1.进入页面
        #2.添加按钮
        #3.填写信息
        #4.确定
        courses = self.home\
            .goto_courses()\
            .add_course(course_name)\
            .get_courses(course_name)
        assert courses != []
        assert courses[0] == course_name

    @pytest.mark.parametrize("class_name", "l班级")  # 参数化
    def test_add_class(self, class_name):
        # 1.进入页面
        # 2.添加按钮
        # 3.填写信息
        # 4.确定
        classes = self.home \
            .goto_classes() \
            .add_class(class_name) \
            .get_class(class_name)
        assert classes != []
        assert classes[0].text == class_name

    @pytest.mark.parametrize("avtivity_name, start_time, end_time", ("l限时折扣活动", "2023-10-02 00:00:00", "2023-10-29 00:00:00"))  # 参数化
    def test_add_avtivity(self, activity_name, start_time, end_time):
        # 1.进入页面
        # 2.添加按钮
        # 3.填写信息
        # 4.确定
        activities = self.home \
            .goto_avtivityes() \
            .add_avtivity(activity_name, start_time, end_time) \
            .get_avtivity(activity_name)
        assert activities != []
        assert activities[0].text == activity_name
