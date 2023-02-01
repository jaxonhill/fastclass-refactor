# sdsu_class_scraper - Run to get all classes at SDSU into pandas dataframe

# Library imports
from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

# Class imports
from classes.DriverInstance import DriverInstance

# Define variables needed
STARTING_PAGE_URL = "https://cmsweb.cms.sdsu.edu/psc/CSDPRD/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_CLSRCH_MAIN_FL.GBL"
TERM_CSS_ID = "TERM_VAL_TBL_DESCR"


def main():
    d: DriverInstance = DriverInstance(STARTING_PAGE_URL)
    print(d.getTermOptions())


if __name__ == "__main__":
    main()
