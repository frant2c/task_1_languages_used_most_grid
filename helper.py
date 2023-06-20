import re
import data

#in future locators can be moved to separete class
#for reducing code duplication character replacements can be done via decorators

def get_table_data(driver, table_headers):
    table = driver.find_element("xpath", "//table")
    rows = table.find_elements("xpath", ".//tbody/tr")
    results = []
    for row in rows:
        cells = row.find_elements("xpath", ".//td")
        row_data = [re.sub(r'\[\d+]', '', cell.text) for cell in cells]
        popularity_str = re.split(r'\s', row_data[1].replace(',', '').replace('.', ''))
        row_data[1] = int(popularity_str[0])
        dict1 = {k: v for k, v in zip(table_headers, row_data)}
        table_data = data.TableData(**dict1)
        results.append(table_data)
    return results
