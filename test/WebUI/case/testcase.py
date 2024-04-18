import pytest
from WebUI.page.login import Login


class TestCase:
    def setup_class(self):

        self.home = Login().login()

    def teardown_class(self):
        self.home.do_quit()

    @pytest.mark.parametrize()  # 参数化
    def test_case1(self):
        pass
        # res = class().method()
        # assert "" == res
