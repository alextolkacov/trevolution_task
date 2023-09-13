import allure

from main.context.ui import UI
from main.enums.locators.buttons import Buttons
from main.enums.locators.containers import Containers
from main.enums.locators.values import Values
from main.pages.booking_information_page import BookingInformationPage


class YourTripPopup(UI):
    def __init__(self, browser):
        super().__init__(browser)
        self.wait_until_page_is_complete()
        assert self.is_element_present(Containers.YOUR_TRIP_POPUP)

    @allure.step('Get flight price from the popup')
    def get_flight_price_from_the_popup(self):
        return self.get_text(Values.PRICE_IN_POPUP)

    @allure.step('Click on \'Book flight\'')
    def click_on_book_flight(self):
        self.click(Buttons.BOOK_FLIGHT_IN_POPUP)
        return BookingInformationPage(self.browser)
