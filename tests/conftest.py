import pytest
from selene import browser
from selenium import webdriver
from data.data import SelenoidData
from helpers import attach


@pytest.fixture(scope = 'function', autouse = True)
def remote_browser():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--headless')
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver_options = options
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "125.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)
    browser.config.driver = webdriver.Remote(
        command_executor = f"https://{SelenoidData.SELENOID_LOGIN}:{SelenoidData.SELENOID_PASS}@{SelenoidData.SELENOID_URL}",
        options = options)
    yield
    attach.add_screenshot()
    attach.add_html()
    attach.add_logs()
    attach.add_video()
    browser.quit()
