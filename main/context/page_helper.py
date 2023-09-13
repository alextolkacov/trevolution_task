from datetime import datetime

import allure

from main.context.ui import UI
from main.enums.locators.buttons import Buttons


def convert_date(date):
    return datetime.strptime(date, '%Y-%m-%d').strftime('%a, %b %-d')


class PageHelper(UI):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Accept all cookies')
    def accept_all_cookies(self):
        self.wait_until_present(Buttons.ACCEPT_ALL_COOKIES)
        self.click(Buttons.ACCEPT_ALL_COOKIES)
