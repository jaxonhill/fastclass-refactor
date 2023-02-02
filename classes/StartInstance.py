from classes.DriverInstance import DriverInstance


STARTING_PAGE_URL: str = "https://cmsweb.cms.sdsu.edu/psc/CSDPRD/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_CLSRCH_MAIN_FL.GBL"


class StartInstance(DriverInstance):
    """
    This is a sub class of DriverInstance and is used to create an original driver
    that will find the different categories we need to loop through and set the term.
    """

    # def __init__(self, url: str):
    #     super().__init__(url)

    def __init__(self):
        super().__init__(STARTING_PAGE_URL)
