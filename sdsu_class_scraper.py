# sdsu_class_scraper - Run to get all classes at SDSU into pandas dataframe

# Class imports
from classes.DriverInstance import DriverInstance

# Define variables needed
STARTING_PAGE_URL = "https://cmsweb.cms.sdsu.edu/psc/CSDPRD/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_CLSRCH_MAIN_FL.GBL"
TERM_CSS_ID = "TERM_VAL_TBL_DESCR"


def main():
    d: DriverInstance = DriverInstance(STARTING_PAGE_URL)
    print(d.getDriver())
    # # Find the term and print it
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "TERM_VAL_TBL_DE"))
    # )


if __name__ == "__main__":
    main()
