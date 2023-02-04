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

    # Go to each category and grab all the links and make a hashmap of information
    for category in categories:
        start_driver.navigateToCategoryPage(category)

    # TODO: LCS has no classes, add error checking

    # Wait for <ul> to show up that has all the classes
    # If it doesn't show up for like 20 seconds, then we have no classes for that category
    # move on to the next

    # Once ul is there, then get rid of the "Open Classes option"

    # Again wait for <ul> to show up
    # If it doesn't show up for like 20 seconds again, then no classes for that category

    # Now, we can check that we aren't past the limit of classes (red text)

    # If we are, then re-search with new parameters such as a 1 in the course name, redo all above stuff
    # If we still have even more problems, then add a 10 after

    # If there is no red text,
    # Then scrape all links of every li under the ul we found originally and store
    # in a hashmap with extra information we might use later


if __name__ == "__main__":
    main()
