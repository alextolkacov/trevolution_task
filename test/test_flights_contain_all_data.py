import logging

from pytest_check import equal

from main.context import page_helper
from main.navigation.start_test import StartTest

logger = logging.getLogger()


class TestFlightsContainAllData:

    def test_flights_contain_all_data(self, browser):
        logger.info('Start test via direct URL')
        search_result_page = StartTest(browser) \
            .via_direct_url() \
            .show_all_results()

        logger.info('Check that every found flight contains price '
                    '& Departure date is the same as from date '
                    'which is in the URL(2023-11-07)')
        equal(search_result_page.get_result_count(),
              len(search_result_page.get_prices()))
        for date in search_result_page.get_dates_from_search_elements(
                search_result_page.get_search_results()):
            equal(page_helper.convert_date('2023-11-07'), date)
