import allure
from jsonpath import jsonpath

from Interface.apis.functions.ims_courses import Courses
from Interface.utils.query_db import QueryDB
from Interface.utils.read_data import GetData


@allure.feature("课程管理")
class TestAddCourse:

    def setup_class(self):
        # 实例化
        self.course = Courses()
        self.db = QueryDB()
        self.getdata = GetData()

        # 准备数据
        self.course_name = "inf课程"
        material_img_uuid = self.db.query_db_one(
            "SELECT uuid FROM ss65_ims.material where file_type = 'img' limit 1;"
        )
        material_video_uuid = self.db.query_db_one(
            "SELECT uuid FROM ss65_ims.material where file_type = 'video' limit 1;"
        )

        self.add_data = {
            "group": self.course.get_courses_group(),
            "name": self.course_name,
            "cover": material_img_uuid,
            "video": material_video_uuid,
            "detail": material_img_uuid,
            "buy_tip": material_img_uuid
        }
        self.data = self.getdata.update_data_json("datas/courses.json", self.add_data)

    def teardown_class(self):
        self.getdata.file_data_init("datas/courses.json", "datas/courses_init.json")

    @allure.story("课程的增删查")
    def test_course(self):
        with allure.step("添加课程"):
            r = self.course.course_create(self.data)
            assert r.status_code == 200
            assert r.json().get("status") == 0
            course_uuid = r.json()["data"]["uuid"]

        with allure.step("查询添加课程结果"):
            r = self.course.course_get()
            name_list = jsonpath(r.json(), "$..name")
            assert self.course_name in name_list

        with allure.step("删除添加的课程"):
            r = self.course.course_delete(course_uuid)
            assert r.status_code == 200
            assert r.json().get("status") == 0
