import pytest
from WebUI.page.login import Login


class TestCase:
    def setup_class(self):

        self.home = Login().login("18842665578", "shanshui65")

    def teardown_class(self):
        self.home.do_quit()

    """def setup(self):
        self.home.goto_url(self.home._BASE_URL)"""

    @pytest.mark.parametrize("course_name", ["l课程"])  # 参数化
    def test_add_course(self, course_name):
        # 1.进入页面
        # 2.添加按钮
        # 3.填写信息
        # 4.确定
        courses = self.home\
            .goto_courses()\
            .add_course(course_name)\
            .get_courses(course_name)
        assert courses != []
        assert courses[0] == course_name

    @pytest.mark.parametrize("class_name", ["l班级"])  # 参数化
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

    @pytest.mark.parametrize("activity_name, start_time, end_time", [("l限时折扣活动", "2023-10-02 00:00:00", "2023-10-29 00:00:00")])  # 参数化
    def test_add_activity(self, activity_name, start_time, end_time):
        # 1.进入页面
        # 2.添加按钮
        # 3.填写信息
        # 4.确定
        activities = self.home \
            .goto_activities() \
            .add_activity(activity_name, start_time, end_time) \
            .get_activity(activity_name)
        assert activities != []
        assert activities[0].text == activity_name
