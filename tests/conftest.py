import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope = "function", autouse = True)
def init_browser():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--headless')
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver_options = options
    yield
    browser.quit()
