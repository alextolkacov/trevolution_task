from selenium.webdriver.common.by import By


class Buttons:
    ACCEPT_ALL_COOKIES = (By.XPATH,
                          ".//button[@id = 'onetrust-accept-btn-handler']")
    SHOW_ALL_RESULTS = (By.XPATH,
                        ".//button[@class = 'result_deals_dealsShowMore__"
                        "8DqRu qa-moreResultsBtn']")
    BOOK_FLIGHT_IN_POPUP = (By.XPATH, ".//div[@class = 'm-r-12 m-l-12']")
