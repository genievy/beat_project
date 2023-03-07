import allure
from pages.elements_page import TestWordFileSelected
from data.data import Url as url
from locators.elements_locators import PageElements, DropDownSelectAttribute, DropDownSelectLocators


@allure.suite("Test elements of Home Page")
class TestDemoqa:
    @allure.feature('Testing test-case 1.0')
    class TestcasesFlows:
        elements = PageElements()
        locators = DropDownSelectLocators()
        attribute = DropDownSelectAttribute()

        def test_word_file_selected(self, driver):
            page = TestWordFileSelected(driver, url.home_page)
            # Testing the pening the home page'

            page.open()
            # Checking the homepage for consistency
            assert page.check_is_page_current(url.home_page), "Home page not found"

            # Checking the Elements page for consistency
            page.open_elements()
            assert page.check_is_page_current(url.elements_page), "Elements page is not opened"

            # Checking the Chekbox page for consistency
            page.open_checkbox()
            assert page.check_is_page_current(url.checkbox_page), "Checkbox page is not opened"

            # Checking the Home directory for click-open
            page.open_home()
            assert page.button_home_value() == page.attribute.OPEN_DIR_VALUE, "Home directory is not expanded"

            # Check the Downloads directory to open on click
            page.open_downloads()
            assert page.button_downloads_value() == page.attribute.OPEN_DIR_VALUE, "Downloads directory is not expanded"

            # Check the activation of the checkbox by clicking in the field
            page.choose_word_file()
            assert page.checkbox_word_file_value() == page.attribute.CHECKBOX_ON_VALUE, \
                "Checkbox 'Word File.doc' is not selected"

            # Check the file selection message to be displayed when the checkbox is activated
            assert page.check_message_visible(),  "File selection message isn`t displayed"
