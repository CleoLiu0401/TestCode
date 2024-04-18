import pytest

def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

@pytest.fixture(scope="function",autouse=True,params=[(99,99),(-99,-99),(99.01,99.01),(-99.01,-99.01)],ids=["最大合法边界","最小合法边界","正非法边界","负非法边界"])
#@pytest.mark.parametrize("a,b", [(99, 99), (-99, -99), (99.01, 99.01), (-99.01, -99.01)],ids=["最大合法边界", "最小合法边界", "正非法边界", "负非法边界"])
def fixture_func():
    print("开始计算")
    yield
    print("结束计算")

@pytest.fixture(scope="session")
def fixture_sess():
    yield
    print("结束测试")