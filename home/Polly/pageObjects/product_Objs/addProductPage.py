from common.basePage import BasePage
from pageObjects.login_Objs import loginPage
from pageObjects.main_Objs import mainPage


class AddProductPage(BasePage):
    def add_product(self, kidx1, kidx2, kidx3, product_name, subtitle):
        self.click_element(self.product_kind)
        self.select_lev1[-1] = self.select_lev1[-1].format(kidx1)
        self.click_element(self.select_lev1)
        self.select_lev2[-1] = self.select_lev2[-1].format(kidx2)
        self.click_element(self.select_lev2)
        self.input_text(self.product_name, product_name)
        self.input_text(self.subtitle, subtitle)
        self.click_element(self.product_brand)
        self.select_idx[-1] = self.select_idx[-1].format(kidx3)
        self.click_element(self.select_idx)
        self.click_element(self.sales_button)
        self.click_element(self.attr_button)
        self.click_element(self.choose_button)
        self.click_element(self.submit_button)
        self.click_element(self.alert_true)


if __name__ == '__main__':
    test_loginpage = loginPage.LoginPage().open_polly_loginpage().login_polly('松勤老师', '123456')
    test_mainpage = mainPage.MainPage()
    test_mainpage.goto_addproductpage()
    test_addproduct = AddProductPage()
    test_addproduct.add_product(kidx1=1, kidx2=1, kidx3=1, product_name='001', subtitle='002')
