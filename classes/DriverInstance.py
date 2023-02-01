# Library imports
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverInstance:
    """
    Create selenium driver object.

    :param url: str -- The URL you want the driver to go to upon creation.
    """

    def __init__(self, url: str):
        self.url = url
        # Create driver on object creation
        self.driver = self.__createDriver(self.url)

    def __createDriver(self, url: str) -> WebDriver:
        # Open selenium and go to the classes URL
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
        return driver

    # TODO: FIX THIS
    def isElementFoundAfterWait(self, css_selector_id: str, wait_time: int) -> bool:
        """
        Wait for an element to appear on the screen, return if it showed up

        :param css_selector_id -- The CSS selector to locate the element
        :param wait_time -- How long (in seconds) to wait for the element to appear
        :return True if found, False if not found after amount of wait_time
        """
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector_id))
            )
            return True
        finally:
            return False

    def getTermOptions(self) -> List[str]:
        """
        Get the term options that are possible to scrape.

        :return List of all possible terms
        """

        # if not self.isElementFoundAfterWait(
        #     "#win0divSSR_CSTRMCUR_GRD\$grid\$0 > table", 10
        # ):
        #     return [""]

        current_terms_table_element: WebElement = self.driver.find_elements(
            By.CLASS_NAME, "ps_grid-flex"
        )[1]
        possible_terms_link_elements: List[WebElement] = list(
            current_terms_table_element.find_elements(By.TAG_NAME, "a")
        )
        return list(map(lambda term: str(term.text), possible_terms_link_elements))
