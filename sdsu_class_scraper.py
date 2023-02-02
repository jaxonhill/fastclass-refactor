# sdsu_class_scraper - Run to get all classes at SDSU into pandas dataframe

# Library imports
from typing import List

# Class imports
from classes.DriverInstance import DriverInstance

# Final, constant variables
STARTING_PAGE_URL = "https://cmsweb.cms.sdsu.edu/psc/CSDPRD/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_CLSRCH_MAIN_FL.GBL"


def main():
    d: DriverInstance = DriverInstance(STARTING_PAGE_URL)
    print(d.getTermOptions())


if __name__ == "__main__":
    main()
