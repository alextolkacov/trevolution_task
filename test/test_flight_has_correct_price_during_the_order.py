import logging

from pytest_check import equal

from main.navigation.start_test import StartTest

logger = logging.getLogger()


class TestFlightHasCorrectPriceDuringTheOrder:
    def test_flight_has_correct_price_during_the_order(self, browser):
        logger.info('Start test via direct URL and get first flight price')
        search_result_page = StartTest(browser) \
            .via_direct_url()
        flight_price = search_result_page.get_flight_price(0)

        logger.info('Click on a first flight option,'
                    'get \'Your trip\' popup and get the price from it')
        your_flight_popup = search_result_page.click_on_flight(0)
        flight_price_in_popup = your_flight_popup \
            .get_flight_price_from_the_popup()

        logger.info(
            'Click \'Book flight\', get booking information page '
            'and get total flight price')
        flight_price_from_booking_ingo_page = your_flight_popup \
            .click_on_book_flight() \
            .get_flight_price()

        logger.info(
            'Check that all prices are similar during the order process')
        equal(flight_price, flight_price_in_popup)
        equal(flight_price_from_booking_ingo_page, flight_price_in_popup)
