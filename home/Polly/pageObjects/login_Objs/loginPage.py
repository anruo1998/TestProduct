import time

from common.basePage import BasePage
from configs.env import Env
from pageObjects.main_Objs import mainPage


class LoginPage(BasePage):
    def open_polly_loginpage(self, url=Env.HOST):
        self.open_url(url)
        return self

    def login_polly(self, username, password):
        self.input_text(self.username, username)
        self.input_text(self.password, password)
        self.click_element(self.login_button)
        return mainPage.MainPage()


if __name__ == '__main__':
    test_loginpage = LoginPage()
    test_loginpage.open_polly_loginpage()
    test_loginpage.login_polly('松勤老师', '123456')
    time.sleep(3)
