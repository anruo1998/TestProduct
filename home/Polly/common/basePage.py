from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

from common.comm_driver import CommonDriver
from configs.env import Env
from utils.handle_path import PollyPath
from utils.handle_yaml import get_yaml_data


class BasePage:
    def __init__(self):
        self.driver = CommonDriver().get_driver()
        self.locators = get_yaml_data(PollyPath.configs_path / 'all_elements.yaml')[self.__class__.__name__]
        for element_name, locator in self.locators.items():
            setattr(self, element_name, locator)

    def open_url(self, url):
        self.driver.get(url)

    def get_element(self, locator, timeout=Env.TIME_OUT, poll_frequency=Env.POLL_FREQUENCY,
                    elements=False):
        try:
            if not elements:
                return WebDriverWait(self.driver, timeout, poll_frequency) \
                    .until(ES.visibility_of_element_located(locator))
            else:
                return WebDriverWait(self.driver, timeout, poll_frequency) \
                    .until(ES.visibility_of_all_elements_located(locator))
        except:
            return False

    def input_text(self, locator, text, append=False):
        if append:
            self.get_element(locator).send_keys(text)
        else:
            self.get_element(locator).clear()
            self.get_element(locator).send_keys(text)

    def click_element(self, locator):
        self.get_element(locator).click()

    def get_element_text(self,locator):
        return self.get_element(locator).text

    def get_element_texts(self,locator):
        elements = self.get_element(locator,elements=True)
        return [ ele.text for ele in elements]

    def is_that_url(self, url, timeout=Env.TIME_OUT, poll_frequency=Env.POLL_FREQUENCY):
        try:
            return WebDriverWait(self.driver, timeout, poll_frequency).until(ES.url_to_be(url))
        except:
            return False

    def has_element_attr_text(self, locator, attr, text, timeout=Env.TIME_OUT, poll_frequency=Env.POLL_FREQUENCY):
        try:
            return WebDriverWait(self.driver, timeout, poll_frequency).until(
                ES.text_to_be_present_in_element_attribute(locator, attr, text))
        except:
            return False


if __name__ == '__main__':
    from pageObjects.login_Objs import loginPage
    test_loginpage = loginPage.LoginPage()
    print(test_loginpage.locators)
