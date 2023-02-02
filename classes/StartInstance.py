# Libraries
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
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

    def clickChosenTerm(self, term):
        term_link: WebElement = self.driver.find_element(By.LINK_TEXT, term)
        term_link.click()
        time.sleep(10)
