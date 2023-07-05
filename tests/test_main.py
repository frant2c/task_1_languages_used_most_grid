import pytest

@pytest.mark.parametrize("test_value",
                         [10 ** 7, 15 * 10 ** 6, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 15 * 10 ** 8])
def test_popularity_of_programming_languages(test_value, parse_table):
    results = parse_table
    for result in results:
        assert result.popularity >= test_value, f"{result.websites} (Frontend: {result.frontend}|Backend:" \
                                                f"{result.backend}) has {result.popularity}) unique visitors " \
                                                f"per month. (Expected more than {test_value})"
