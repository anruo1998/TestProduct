import allure
import pytest

from utils.handle_path import PollyPath
from utils.handle_rand_str import get_rand_str
from utils.handle_yaml import get_yaml_data

addproduct_all_datas = get_yaml_data(PollyPath.testDatas_path / 'addproduct_all-datas.yaml')

@allure.epic('史诗：Polly')
@allure.feature('特性：商品管理模块')
@allure.story('用户故事：添加商品模块')
# @pytest.mark.parametrize('kidx1, kidx2, kidx3, product_name, subtitle',)

def test_addproduct_success(fix_login_polly, kidx1, kidx2, kidx3):
    allure.title('添加奖品成功')
    with allure.step('1、用户已登录'):
        test_mainpage = fix_login_polly
    with allure.step('2、打开添加商品页面'):
        test_addproduct_page = test_mainpage.is_Menu_button().goto_addproductpage()
    with allure.step('3、添加商品'):
        input_productname = '商品名' + get_rand_str(5)
        input_subtitle = '副标题' + get_rand_str(5)
        test_addproduct_page.add_product(kidx1, kidx2, kidx3, input_productname, input_subtitle)
    # with allure.step('4、断言'):



