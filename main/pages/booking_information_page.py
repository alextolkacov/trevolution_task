import allure

from main.context.ui import UI
from main.enums.locators.containers import Containers
from main.enums.locators.values import Values


class BookingInformationPage(UI):

    def __init__(self, browser):
        super().__init__(browser)
        self.wait_until_page_is_complete()
        assert self.is_element_present(Containers.PRICE_SUMMARY_BLOCK)

    @allure.step('Get flight price')
    def get_flight_price(self):
        return self.get_text(Values.TOTAL_PRICE_ON_BOOKING_INFO_PAGE)
