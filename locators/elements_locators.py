from selenium.webdriver.common.by import By


class PageElements:
    ELEMENTS = (By.CSS_SELECTOR, "[class*='category']>div:nth-child(1)")
    CHECK_BOX = (By.CSS_SELECTOR, "[class*='element-list collapse show']>ul>li:nth-child(2)")
    HOME_TOGGLE_BUTTON = (By.CSS_SELECTOR, "#tree-node > ol > li > span > button")
    DOWNLOADS_TOGGLE_BUTTON = (By.CSS_SELECTOR, "#tree-node>ol>li>ol>li:nth-child(3)>span>button")
    HOME_CHECKBOX = (By.XPATH, "//*[@id='tree-node']/ol/li/span/label/span[1]")
    WORD_FILE_CHECKBOX = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg")
    RESULT = (By.CSS_SELECTOR, "#result")

class DropDownSelectLocators:
    HOME_DIR = (By.XPATH, "//*[@id='tree-node']/ol/li")
    DOWNLOADS_DIR = (By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[3]")

class DropDownSelectAttribute:
    ATTR_NAME: str = "class"
    CLASS_NAME: str = "class"
    OPEN_DIR_VALUE: str = 'rct-node rct-node-parent rct-node-expanded'
    CHECKBOX_ON_VALUE: str = "rct-icon rct-icon-check"
    TEXT_CONTENT: str = "textContent"
