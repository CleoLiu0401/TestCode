import allure

from Interface.apis.functions.ics_courses import Courses
from Interface.apis.functions.ics_order import Order
from Interface.apis.functions.ics_students import Students
from Interface.utils.read_data import GetData


class TestOrder:

    def setup_class(self):
        # 实例化
        self.order = Order()
        self.student = Students()
        self.course = Courses()
        self.getdata = GetData()

        # 准备数据
        student_uuid = self.student.get_student()
        course_uuid = self.course.get_courses()
        self.cart_data = {
            "student": student_uuid,
            "goods": course_uuid,
            "goods_type": "educourse",
            "goods_number": 1
        }

    def teardown_class(self):
        self.getdata.file_data_init("datas/settle.json", "datas/settle_init.json")

    @allure.story("下单购买")
    def test_order(self):
        with allure.step("加入购物车"):
            r = self.order.cart_add(self.cart_data)
            assert r.status_code == 200
            assert r.json().get("status") == 0
            goods_uuid = r.json()["data"]["uuid"]

        with allure.step("下单结算"):
            r = self.order.order_settle(goods_uuid)
            assert r.status_code == 200
            assert r.json().get("status") == 0
            # data取自结算结果+order_type
            pay_data = self.getdata.update_data_json("datas/settle.json", r.json())

        """with allure.step("支付"):
            r = self.order.order_pay(pay_data)
            assert r.status_code == 200
            assert r.json().get("status") == 0"""
