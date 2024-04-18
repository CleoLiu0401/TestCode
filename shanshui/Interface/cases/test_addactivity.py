import time

import allure

from Interface.apis.functions.ims_activities import Activities
from Interface.apis.functions.ims_courses import Courses
from Interface.utils.read_data import GetData


@allure.feature("活动管理")
class TestAddActivity:

    def setup_class(self):
        # 实例化
        self.activity = Activities()
        self.course = Courses()
        self.getdata = GetData()
        # 准备数据
        self.activity_name = "inf活动"
        self.start_time = int(time.time())
        self.end_time = self.start_time + 30 * 24 * 60 * 60
        self.course_uuid = self.course.get_course_uuid("课程1")

        self.add_data = {

            "name": self.activity_name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "educourses": [
                {
                    "uuid": self.course_uuid,
                    "special_price": 0.01
                }
            ]
        }
        self.data = self.getdata.update_data_json("datas/activity_discount.json", self.add_data)

    def teardown_class(self):
        self.getdata.file_data_init("datas/activity_discount.json", "datas/activity_discount_init.json")

    @allure.story("添加限时折扣活动")
    def test_activity_add(self):
        with allure.step("添加限时折扣活动"):
            r = self.activity.activity_discount_create(self.data)
            assert r.status_code == 200
            assert r.json().get("status") == 0
            activity_uuid = r.json()["data"]["uuid"]

        with allure.step("查询添加活动结果"):
            r = self.activity.activity_discount_get(self.activity_name)
            assert r.json()["data"]["records"][0]["name"] == self.activity_name

        with allure.step("删除添加的活动"):
            r = self.activity.activity_discount_delete(activity_uuid)
            assert r.status_code == 200
            assert r.json().get("status") == 0
