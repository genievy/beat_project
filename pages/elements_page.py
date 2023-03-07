import allure
from pages.base_objects import BaseObjects
from locators.elements_locators import PageElements, DropDownSelectAttribute, DropDownSelectLocators


class TestWordFileSelected(BaseObjects):
    elements = PageElements()
    locators = DropDownSelectLocators()
    attribute = DropDownSelectAttribute()

    @allure.step("Клик на элементе страницы после тайтаута на его визуализацию")
    def open_elements(self):
        self.element_visible(self.elements.ELEMENTS).click()

    @allure.step("Проверка url страницы на соответствие")
    def check_is_page_current(self, check_url):
        return True if self.get_current_url() == check_url else False

    @allure.step("Активация чекбокса")
    def open_checkbox(self):
        self.element_visible(self.elements.CHECK_BOX).click()

    @allure.step("Разворачиваем директорию Home")
    def open_home(self):
        self.element_visible(self.elements.HOME_TOGGLE_BUTTON).click()

    @allure.step("Разворачиваем директорию Downloads")
    def open_downloads(self):
        self.element_visible(self.elements.DOWNLOADS_TOGGLE_BUTTON).click()

    @allure.step("Активация чекбокса WordFile")
    def choose_word_file(self):
        self.element_visible(self.elements.WORD_FILE_CHECKBOX).click()

    @allure.step("Проверка появление сообщения")
    def check_message_visible(self):
        return True if self.element_visible(self.elements.RESULT) else False

    @allure.step("Проверка, что  директория Home открыта")
    def button_home_value(self):
        return self.get_attribute_by_locator(self.locators.HOME_DIR, self.attribute.CLASS_NAME)

    @allure.step("Проверка, что директория Downloads открыта")
    def button_downloads_value(self):
        return self.get_attribute_by_locator(self.locators.DOWNLOADS_DIR, self.attribute.CLASS_NAME)

    @allure.step("Проверка, что чекбокс Word File открыт")
    def checkbox_word_file_value(self):
        return self.get_attribute_by_locator(self.elements.WORD_FILE_CHECKBOX, self.attribute.CLASS_NAME)

    @allure.step("Проверка, содержимого текста сообщения")
    def check_text_message(self):
        return self.get_attribute_by_locator(self.elements.RESULT, self.attribute.TEXT_CONTENT)






