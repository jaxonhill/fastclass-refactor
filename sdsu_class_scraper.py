# sdsu_class_scraper - Run to get all classes at SDSU into pandas dataframe
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define variables needed
ORIGINAL_URL = "https://cmsweb.cms.sdsu.edu/psc/CSDPRD/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_CLSRCH_MAIN_FL.GBL"
TERM_CSS_ID = "TERM_VAL_TBL_DESCR"


def main():
    # Open selenium and go to the classes URL
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(ORIGINAL_URL)

    # Find the term and print it
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "TERM_VAL_TBL_DE"))
    )


if __name__ == "__main__":
    main()
