import pytest
from selenium import webdriver


@pytest.fixture(scope='module')
def instanceofdriver() -> webdriver:
    """
    driver initializing
    """
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
