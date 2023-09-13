from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class UI:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 15)

    def open_page(self, url):
        match url:
            case url if url.startswith('http://') or \
                        url.startswith('https://'):
                self.browser.get(url)
            case _:
                self.browser.get('https://' + url)

    def wait_until_present(self, locator):
        self.wait.until(
            ec.presence_of_all_elements_located(locator))

    def wait_until_invisible(self, locator, timeout=15):
        WebDriverWait(self.browser, timeout=timeout).until(
            ec.invisibility_of_element(locator))

    def wait_to_be_clickable(self, locator):
        self.wait.until(
            ec.element_to_be_clickable(locator))

    def get_element(self, locator):
        assert len(self.get_elements(locator)) != 0, 'No elements found'
        return self.get_elements(locator)[0]

    def get_elements(self, locator, wait=True):
        if wait:
            self.wait_until_present(locator)
        return self.browser.find_elements(locator[0], locator[1])

    def get_text(self, locator):
        return self.get_element(locator).text

    def click(self, locator):
        self.wait_to_be_clickable(locator)
        self.get_element(locator).click()

    def is_element_present(self, locator):
        return len(self.get_elements(locator)) != 0

    def wait_until_page_is_complete(self):
        self.wait.until(
            lambda x: x.execute_script(
                'return document.readyState') == 'complete')

    def get_element_in_element(self, el, locator):
        self.wait_until_present(locator)
        return el.find_element(locator[0], locator[1])

    def is_element_present_on_page(self, locator, wait=False):
        if wait:
            self.wait_until_page_is_complete()
        return len(self.browser.find_elements(locator[0], locator[1])) != 0
