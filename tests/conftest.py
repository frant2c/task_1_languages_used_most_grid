import pytest

from helpers.helper import get_table_data, map_table_data

TABLE_HEADERS = ["websites", "popularity", "frontend", "backend", "database", "notes"]
BASE_URL = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most _popular_websites"


@pytest.fixture(scope='module')
def parse_table(instanceofdriver) -> list[dict]:
    instanceofdriver.get(BASE_URL)
    raw_data = get_table_data(instanceofdriver, TABLE_HEADERS)
    parse_table = map_table_data(raw_data)
    return parse_table
