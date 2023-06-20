import pytest
from selenium import webdriver

from helper import get_table_data

TABLE_HEADERS = ["websites", "popularity", "frontend", "backend", "database", "notes"]
BASE_URL = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most _popular_websites"


@pytest.mark.parametrize("test_value",
                         [10 ** 7, 15 * 10 ** 6, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 15 * 10 ** 8])
def test_popularity_of_programming_languages(test_value):
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    results = get_table_data(driver, TABLE_HEADERS)
    for result in results:
        assert result.popularity >= test_value, f"{result.websites} (Frontend: {result.frontend}|Backend:" \
                                                f"{result.backend}) has {result.popularity}) unique visitors " \
                                                f"per month. (Expected more than {test_value})"
    driver.quit()
