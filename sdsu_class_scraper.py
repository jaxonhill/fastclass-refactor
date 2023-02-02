# sdsu_class_scraper - Run to get all classes at SDSU into pandas dataframe

# Library imports
from typing import List

# Class imports
from classes.DriverInstance import DriverInstance
from classes.StartInstance import StartInstance


def main():
    start_driver: StartInstance = StartInstance()
    print(start_driver.getTermOptions())


if __name__ == "__main__":
    main()
