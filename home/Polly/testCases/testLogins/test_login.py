import allure
import pytest

from configs.allElements import AllElements
from configs.env import Env
from pageObjects.login_Objs.loginPage import LoginPage
from utils.handle_path import PollyPath
from utils.handle_yaml import get_yaml_data

login_all_data = get_yaml_data(PollyPath.testDatas_path / 'login_all_datas.yaml')

@allure.epic('史诗：Polly')
@allure.feature('特性：用户中心模块')
@allure.story('用户故事：登录功能测试')
@pytest.mark.parametrize('title,username,password,expected_locator,expected_text', login_all_data)
def test_login_v1(title, username, password, expected_locator, expected_text):
    allure.dynamic.title(title)
    with allure.step('1. 打开网页'):
        test_loginpage = LoginPage()
    with allure.step('2. 打开宝利商城'):
        test_loginpage.open_polly_loginpage()
    with allure.step('3. 登录宝利商城'):
        test_loginpage.login_polly(username, password)
    with allure.step('4. 断言'):
        with pytest.assume: assert test_loginpage.get_element_text(expected_locator) == expected_text
    with allure.step('5. 断言后处理'):
        if test_loginpage.is_that_url(Env.MAIN_URL):
            test_loginpage.click_element(AllElements.USER_BUTTON)
            test_loginpage.click_element(AllElements.QUIT_BUTTON)
            from time import sleep
            sleep(1)

if __name__ == '__main__':
    pytest.main(['-sv',__file__])