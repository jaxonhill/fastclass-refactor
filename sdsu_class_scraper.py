# sdsu_class_scraper - Run to get all classes at SDSU into pandas dataframe

# Library imports
from typing import List

# Class imports
from classes.DriverInstance import DriverInstance
from classes.StartInstance import StartInstance


def main():
    # Create the start driver and select a term based on user choice
    start_driver: StartInstance = StartInstance()
    # TODO: Error checking the term choice based on the options??
    term_choice: str = input(f"{start_driver.getTermOptions()}\n")
    start_driver.clickChosenTerm(term_choice)

    # TODO: Get all possible categories and store in an array


if __name__ == "__main__":
    main()
