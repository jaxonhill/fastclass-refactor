# Library imports
from selenium import webdriver
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
