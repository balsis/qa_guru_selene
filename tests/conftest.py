import pytest
from selene import browser
from selenium import webdriver
from data.data import SelenoidData
from helpers import attach


@pytest.fixture(scope = 'function', autouse = True)
def remote_browser(request):
    options = webdriver.ChromeOptions()
    # options.page_load_strategy = 'eager'
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument('--headless')
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    browser.config.driver = webdriver.Remote(
        command_executor = f"https://{SelenoidData.SELENOID_LOGIN}:{SelenoidData.SELENOID_PASS}@{SelenoidData.SELENOID_URL}/wd/hub",
        options = options)
    browser.config.driver_options = options
    browser.config.base_url = 'https://demoqa.com'
    yield browser
    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
