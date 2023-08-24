import time

from common.basePage import BasePage
from pageObjects.login_Objs import loginPage
from pageObjects.product_Objs import addProductPage, productListPage


class MainPage(BasePage):
    def is_Menu_button(self):
        if self.has_element_attr_text(self.Menu_button,'class', 'is-active'):
            pass
        else:
            self.click_element(self.Menu_button)


    def goto_addproductpage(self):
        if self.has_element_attr_text(self.menu_product_fold,'class', 'is-opened'):
            self.click_element(self.addProduct)
            return addProductPage.AddProductPage()
        else:
            self.click_element(self.menu_product_fold)
            self.click_element(self.addProduct)
            return addProductPage.AddProductPage()

    def goto_productlistpage(self):
        if self.has_element_attr_text(self.menu_product_fold,'class', 'is-opened'):
            self.click_element(self.product_list)
            return productListPage.ProductListPage()
        else:
            self.click_element(self.menu_product_fold)
            self.click_element(self.product_list)
            return productListPage.ProductListPage()

if __name__ == '__main__':
    test_loginpage = loginPage.LoginPage().open_polly_loginpage().login_polly('松勤老师', '123456')
    test_mainpage = MainPage()
    test_mainpage.goto_addproductpage()
