from selenium import webdriver

from configs.env import Env


# 单例实现
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # 如果没有单例，则新建一个单例，放置在 _instance 中
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# 浏览器实例化
class CommonDriver(Singleton):
    driver = None

    def get_driver(self, browser_type=Env.BROWSER_TYPE, headless_flag=Env.HEADLESS_FLAG,
                   page_load_timeout=Env.PAGE_LOAD_TIMEOUT):
        # 无头模式
        if self.driver is None:
            if headless_flag:
                if browser_type == 'chrome':
                    self.driver = webdriver.Chrome()
                elif browser_type == 'firefox':
                    self.driver = webdriver.Firefox()
            # 有头模式
            else:
                if browser_type == 'chrome':
                    _option = webdriver.ChromeOptions()
                    _option.add_argument('__headless')
                    self.driver = webdriver.Chrome(options=_option)
                elif browser_type == 'firefox':
                    _option = webdriver.FirefoxOptions()
                    _option.add_argument('__headless')
                    self.driver = webdriver.Firefox(options=_option)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(page_load_timeout)
        return self.driver


if __name__ == '__main__':
    test_flag = 3
    if test_flag == 3:
        d31 = CommonDriver().get_driver()
        d32 = CommonDriver().get_driver()
        print(id(d31))
        print(id(d32))
