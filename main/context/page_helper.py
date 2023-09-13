from datetime import datetime

import allure
from selenium.common import ElementClickInterceptedException

from main.context.ui import UI
from main.enums.locators.buttons import Buttons


def convert_date(date):
    return datetime.strptime(date, '%Y-%m-%d').strftime('%a, %b %-d')


class PageHelper(UI):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Accept all cookies')
    def accept_all_cookies(self):
        if self.is_element_present(Buttons.ACCEPT_ALL_COOKIES):
            try:
                self.click(Buttons.ACCEPT_ALL_COOKIES)
            except ElementClickInterceptedException:
                self.wait_to_be_clickable(Buttons.ACCEPT_ALL_COOKIES)
