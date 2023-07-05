import re

from data.data import TableData


# in future locators can be moved to separate class
# for reducing code duplication character replacements can be done via decorators

def get_table_data(driver, table_headers):
    table = driver.find_element("xpath", "//table")
    rows = table.find_elements("xpath", ".//tbody/tr")
    results = []
    for row in rows:
        cells = row.find_elements("xpath", ".//td")
        dict1 = {k: v.text for k, v in zip(table_headers, cells)}
        results.append(dict1)
    return results


def map_table_data(data):
    result = []
    for d in data:
        updated_data = {key: re.sub(r"\[\d+]", '', value) for key, value in d.items()}
        popularity_str = re.split(r'\s', updated_data["popularity"].replace(',', '').replace('.', ''))
        updated_data["popularity"] = int(popularity_str[0])
        table_data = TableData(**updated_data)
        result.append(table_data)
    return result
