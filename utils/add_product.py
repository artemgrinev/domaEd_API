import asyncio
import csv
from elasticsearch import AsyncElasticsearch, RequestError

from src.domaed_app.db.maps import MAPPING_FOR_PRODUCT

path_to_file = r'../src/domaed_app/data/products.csv'


def get_product_list(path) -> list:
    with open(path, encoding='utf-8') as csvfile:
        csv_read = csv.DictReader(csvfile)
        data = []
        for rows in csv_read:
            data.append(rows)
    return data


async def main():
    elastic_client = AsyncElasticsearch('http://localhost:9200')
    try:
        await elastic_client.indices.create(index="products", mappings=MAPPING_FOR_PRODUCT)
    except RequestError as err:
        print(err)
    for document in get_product_list(path_to_file):
        await elastic_client.index(index="products", document=document)


asyncio.run(main())
