import pytest
from Calculator.DevCode.Calculator import Calculator
import yaml

class Test:

    @pytest.mark.add
    @pytest.mark.parametrize("a,b",[(99,99),(-99,-99),(99.01,99.01),(-99.01,-99.01)],ids=["最大合法边界","最小合法边界","正非法边界","负非法边界"])
    def test_add(self,a,b):
        #实例化
        calc = Calculator()
        result = calc.add(a,b)
        print(f'实际结果为：{result}')
        if a > 99 or a < -99 or b > 99 or b < -99:
            expect = "参数大小超出范围"
        else:
            expect = a+b
        print(f'预期结果为：{expect}')
        assert result == expect

    def test_yamldemo():
        # safe_load() 可将yaml对象转成python对象
        with open("../datas/demo.yaml", encoding="utf-8") as f:
            result = yaml.safe_load(f)
        print(result)

    def test_safe_dump():
        # safe_dump() 可将python对象转成yaml格式
        data = {"add": {"data": [[1, 1, 2], [2, 2, 4]], "ids": ["a", "b"]}}
        with open("../datas/data.yaml", mode="w", encoding="utf-8") as f:
            yaml.safe_dump(data, f)

    def get_datas(level):
        """
        读取yaml文件中的数据
        :param level: 通过 级别获取数据，datas 和ids
        :return:
        """
        with open("../datas/calculator.yaml", encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        p0_datas = datas.get('add').get(level).get('datas')
        p0_ids = datas.get('add').get(level).get('ids')
        return [p0_datas,p0_ids]