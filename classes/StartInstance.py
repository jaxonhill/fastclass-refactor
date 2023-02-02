# Libraries
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Classes
from classes.DriverInstance import DriverInstance


STARTING_PAGE_URL: str = "https://cmsweb.cms.sdsu.edu/psc/CSDPRD/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_CLSRCH_MAIN_FL.GBL"


class StartInstance(DriverInstance):
    """
    This is a sub class of DriverInstance and is used to create an original driver
    that will find the different categories we need to loop through and set the term.
    """

    def __init__(self):
        super().__init__(STARTING_PAGE_URL)

    def clickChosenTerm(self, term) -> None:
        term_link: WebElement = self.driver.find_element(By.LINK_TEXT, term)
        term_link.click()

    def openAdvancedPopUp(self) -> None:
        # Open and click on advanced options pane
        advanced_css_selector: str = "#SSR_CLSRCH_FLDS_PTS_ADV_SRCH"
        if not self.isElementFoundAfterWait(advanced_css_selector, 15):
            return
        advanced_options_element: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, advanced_css_selector
        )
        advanced_options_element.click()

        # Find and switch to iframe of the advanced options
        iframe_element: WebElement = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        self.driver.switch_to.frame(iframe_element)

    def retrieveCategoryList(self) -> List[str]:
        select_css_selector: str = "#SSR_CLSRCH_ADV_SSR_ADVSRCH_OP2\$0"
        if not self.isElementFoundAfterWait(select_css_selector, 10):
            return [""]

        select_category_element: Select = Select(
            self.driver.find_element(By.CSS_SELECTOR, select_css_selector)
        )
        # Return a list of the options' "value" attribute tags
        # These are the class codes for each category
        return list(
            map(
                lambda option: option.get_attribute("value"),
                select_category_element.options,
            )
        )[1:]
