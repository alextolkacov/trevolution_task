from selenium.webdriver.common.by import By


class Containers:
    PROGRESS_BAR = (By.XPATH, ".//div[@id = 'progress-bar-container']")
    SEARCH_RESULT = (By.XPATH,
                     ".//div[@class = 'flex stretch pos-rlt pointer']")
    YOUR_TRIP_POPUP = (By.XPATH,
                       ".//div[@class = "
                       "'pqDetails_result_pqDetailsResultDesk__T5wdC']")
    PRICE_SUMMARY_BLOCK = (By.XPATH, ".//div[@data-qa = '_pricingBlock']")
