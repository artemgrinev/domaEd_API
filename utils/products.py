import csv

path_to_file = r'data/products.csv'


def get_product_list(path) -> list:
    with open(path, encoding='utf-8') as csvfile:
        csv_read = csv.DictReader(csvfile)
        data = []
        for rows in csv_read:
            data.append(rows)
    return data


product_list = get_product_list(path_to_file)
