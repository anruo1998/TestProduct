import pytest

from configs.env import Env
from pageObjects.login_Objs.loginPage import LoginPage


@pytest.fixture(scope='session')
def fix_login_polly():
    print('1.S 宝利商城登录')
    mainpage = LoginPage().open_polly_loginpage().login_polly(Env.USERNAME, Env.PASSWORD)
    yield mainpage
    print('1.S 宝利商城登录清除')


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        # print(item.nodeid) #转换前的信息
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)  # 转换后的信息
