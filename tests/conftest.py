import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope = "function", autouse = False)
def local_browser():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--headless')
    browser.config.base_url = 'https://demoqa.com'
    browser.config.driver_options = options
    yield
    browser.quit()


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
        command_executor = f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options = options)
    yield
    browser.quit()
