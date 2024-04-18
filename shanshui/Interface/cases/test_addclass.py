import time

import allure

from Interface.apis.functions.ims_classes import Classes
from Interface.apis.functions.ims_courses import Courses
from Interface.utils.query_db import QueryDB
from Interface.utils.read_data import GetData


@allure.feature("班级管理")
class TestAddClass:

    def setup_class(self):
        # 实例化
        self.classes = Classes()
        self.course = Courses()
        self.db = QueryDB()
        self.getdata = GetData()

        # 准备数据
        self.class_name = "inf班级"
        self.start_date = int(time.time())
        self.end_date = self.start_date + 30 * 24 * 60 * 60
        # self.course_uuid = self.course.get_course_uuid("inf课程名称")
        self.course_uuid = self.course.course_get().json()["data"]["records"][0]["uuid"]
        self.adviser = self.db.query_db_one(
                "SELECT uuid FROM ss65_race.employee where state = 'on' and role = 'adviser' limit 1;"
            )
        self.supervisor = self.db.query_db_one(
                "SELECT uuid FROM ss65_race.employee where state = 'on' limit 1;"
            )
        self.lecturer = self.db.query_db_one(
                "SELECT uuid FROM ss65_race.employee where state = 'on' and role = 'lecturer' limit 1;"
            )
        self.assistant = self.db.query_db_one(
                "SELECT uuid FROM ss65_race.employee where state = 'on' and role = 'assistant' limit 1;"
            )
        self.add_data = {
            "name": self.class_name,
            "educourse": self.course_uuid,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "adviser": self.adviser,
            "supervisor": self.supervisor,
            "lecturer": self.lecturer,
            "assistant": self.assistant
        }
        self.data = self.getdata.update_data_json("datas/classes.json", self.add_data)

    def teardown_class(self):
        self.getdata.file_data_init("datas/classes.json", "datas/classes_init.json")

    @allure.story("添加班级")
    def test_class(self):
        with allure.step("添加班级"):
            r = self.classes.class_create(self.data)
            assert r.status_code == 200
            assert r.json().get("status") == 0
            class_uuid = r.json()["data"]["uuid"]

        with allure.step("查询添加班级结果"):
            r = self.classes.class_get(self.class_name)
            assert r.json()["data"]["records"][0]["name"] == self.class_name

        """with allure.step("删除添加的班级"):
            # 只能删除未销售或已结束销售的班级
            del_class_uuid = self.db.query_db_one(
                "SELECT * FROM ss65_race.educlass where \
                sale_state !='running' and student_count = 0 and lesson_state != 'wait';"
            )
            r = self.classes.class_delete(del_class_uuid)
            assert r.status_code == 200
            assert r.json().get("status") == 0"""
