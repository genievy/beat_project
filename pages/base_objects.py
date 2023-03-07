from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BaseObjects:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        return self.driver.get(self.url)

    def find_element(self, element):
        return self.driver.find_element(element)

    def element_visible(self, element, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(element))

    # def get_attribute(self, locator, attribute):
    #     script = f'return document.querySelector("{locator}").{attribute}'
    #     return self.driver.execute_script(script)

    # def get_attribute(self, element, attribute):
    #     return self.driver.find_element(element).get_attribute(attribute)

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    def get_attribute_by_locator(self, locator, attribute):
        """
        Функция получения значения атрибута веб-элемента по локатору с помощью JavaScript.

        :param driver: экземпляр WebDriver для управления браузером.
        :param locator: строка локатора элемента.
        :param attribute: строка, представляющая имя атрибута.
        :return: значение атрибута элемента.
        """
        element = wait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.execute_script("return arguments[0].getAttribute(arguments[1]);", element, attribute)

    def get_current_url(self):
        return self.driver.current_url
