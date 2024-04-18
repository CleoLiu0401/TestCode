import os
import allure


@allure.feature("")
class TestFunctionFlow:

    def setup_class(self):
        #实例化
        self.ins = Function()
        #准备数据
        self.create_data = {}
        #读取yaml 获取参数，util的方法
        yaml_path = os.sep.join([GetData.get_fram_root_path(), "config/params.yaml"])
        yaml_data = GetData.get_data(yaml_path)
        #获取需要的值
        params1 = yaml_data.get("params1").get("a")

        self.func = Function(params1)
        self.data = {}

    @allure.story("")
    def test_function_flow(self):
        with allure.step(""):
            r = self.func.create(self.create_data)
            assert r.status_code == 200
            assert r.json().get("errcode") == 0
