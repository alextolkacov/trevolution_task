import platform

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.remote.remote_connection import LOGGER, logging
from webdriver_manager.chrome import ChromeDriverManager

logger = logging.getLogger()


@pytest.fixture
def browser():
    LOGGER.setLevel(logging.WARNING)
    os_name = platform.system()
    options = webdriver.ChromeOptions()
    match os_name:
        case 'Linux':
            options.add_argument('--disable-gpu')
            options.add_argument('--dns-prefetch-disable')
            options.add_argument('--no-sandbox')
            options.add_argument('--log-level=2')
            options.add_argument('--headless')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4444',
                options=options)
            driver.file_detector = LocalFileDetector()
        case 'Darwin' | 'Windows':
            driver = webdriver.Chrome(service=Service(
                ChromeDriverManager().install()))
        case _:
            raise AssertionError(os_name + ' platform is not supported')
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    yield driver
    driver.quit()
