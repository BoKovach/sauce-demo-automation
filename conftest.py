import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from tests.test_login_logout import login_data
from utils.driver_factory import get_driver
import allure
import os


@pytest.fixture(scope='function')
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def create_reports_folder():
    os.makedirs("reports/screenshots", exist_ok=True)


@pytest.fixture()
def login_and_go_to_inventory(driver):
    data = login_data[0]
    login = LoginPage(driver)
    login.open()
    login.login(data['username'], data['password'])

    return InventoryPage(driver)


# Hook for Screenshot for fail
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot_path = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
