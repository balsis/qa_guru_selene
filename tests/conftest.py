import pytest
from selene import browser
from selenium import webdriver
from data.data import SelenoidData
from helpers import attach


@pytest.fixture(scope = 'function', autouse = True)
def remote_browser(request):
    options = webdriver.ChromeOptions()
    browser.config.driver_options = options
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "125.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.page_load_strategy = 'eager'
    options.capabilities.update(selenoid_capabilities)
    browser.config.driver = webdriver.Remote(
        command_executor = f"https://{SelenoidData.SELENOID_LOGIN}:{SelenoidData.SELENOID_PASS}@{SelenoidData.SELENOID_URL}/wd/hub",
        options = options)
    yield browser
    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
