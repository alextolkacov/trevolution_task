import allure

from main.context.ui import UI
from main.enums.locators.buttons import Buttons
from main.enums.locators.containers import Containers
from main.enums.locators.values import Values
from main.pages.your_trip_popup import YourTripPopup


class SearchResultPage(UI):
    def __init__(self, browser):
        super().__init__(browser)
        self.wait_until_page_is_complete()
        assert self.is_element_present(Containers.SEARCH_RESULT)

    @allure.step('Expand to see all results')
    def show_all_results(self):
        while self.is_element_present_on_page(Buttons.SHOW_ALL_RESULTS):
            self.click(Buttons.SHOW_ALL_RESULTS)
        return self

    @allure.step('Get search results')
    def get_search_results(self):
        return self.get_elements(Containers.SEARCH_RESULT)

    @allure.step('Get search result count')
    def get_result_count(self):
        return len(self.get_search_results())

    @allure.step('Get prices')
    def get_prices(self):
        return self.get_elements(Values.PRICE)

    @allure.step('Get dates from search elements')
    def get_dates_from_search_elements(self, els: list) -> list:
        return list(map(lambda x: self.get_element_in_element(x, Values.DATE_FROM).text, els))

    @allure.step('Get {1} flight price')
    def get_flight_price(self, search_result_number):
        return self.get_prices()[search_result_number].text

    @allure.step('Click on the {1} flight')
    def click_on_flight(self, flight_number):
        self.get_search_results()[flight_number].click()
        return YourTripPopup(self.browser)
