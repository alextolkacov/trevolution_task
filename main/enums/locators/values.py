from selenium.webdriver.common.by import By


class Values:
    PRICE = (By.XPATH, ".//div[@data-qa = 'pq-price']")
    DATE_FROM = (By.XPATH, ".//div[@data-qa = 'pqDateFrom']")
    PRICE_IN_POPUP = (By.XPATH,
                      ".//div[@class = 'l-h-1 price f-s-16 t-s-bold']")
    TOTAL_PRICE_ON_BOOKING_INFO_PAGE = (By.XPATH,
                                        ".//div[@data-qa = '_totPrice']")
