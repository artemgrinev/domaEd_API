import asyncio
import json

from db.elasticsearch.maps import product_mappings, settings
from utils.web_crawler.index_builder import Builder


if __name__ == "__main__":
    path_to_file_json = r'../data/products.json'
    host = 'http://localhost:9200'

    with open(path_to_file_json) as f:
        products = json.load(f)

    create_index = Builder(
        host=host,
        name="products1-",
        document=products["data"],
        mappings=product_mappings,
        settings=settings
        )
    index_name = create_index.create_empty_index()
    asyncio.run(create_index.build_new_index(index_name))

