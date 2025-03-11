import allure
import pytest
from selene import browser
from selenium import webdriver
from data.data import SelenoidData
from helpers import attach


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version', help='Выберите версию браузера',
        default='100.0'
    )


@pytest.fixture(scope = 'function', autouse = True)
def remote_browser(request):
    browser_version = request.config.getoption('--browser_version')
    with allure.step(f"Инициализация браузера Chrome с версией {browser_version}"):
        options = webdriver.ChromeOptions()
        browser.config.driver_options = options
        browser.config.base_url = 'https://demoqa.com'
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
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
