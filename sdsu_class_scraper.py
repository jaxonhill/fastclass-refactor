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

    # Open the advanced tab and retrieve all possible categories
    start_driver.openAdvancedPopUp()
    categories: List[str] = start_driver.retrieveCategoryList()
    print(categories)

    # Go to each category and grab all the links
    for category in categories:
        start_driver.navigateToCategoryPage(category)

    # TODO: LCS has no classes, add error checking

    # Wait for <ul> to show up that has all the classes

    # Check that we aren't past the limit of classes (red text)

    # If we are, then hit the buttons to make it so we have all the classes

    # Then scrape all links of every li under the ul we found originally and store
    # in a hashmap with extra information we might use later


if __name__ == "__main__":
    main()
