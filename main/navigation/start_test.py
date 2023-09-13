from main.context.page_helper import PageHelper
from main.context.ui import UI
from main.enums.env import Env
from main.enums.locators.containers import Containers
from main.pages.search_result_page import SearchResultPage


class StartTest:
    def __init__(self, browser):
        self.browser = browser

    def via_direct_url(self):
        self.browser.get(Env.DIRECT_URL)
        UI(self.browser).wait_until_invisible(locator=Containers.PROGRESS_BAR)
        PageHelper(self.browser).accept_all_cookies()
        return SearchResultPage(self.browser)
