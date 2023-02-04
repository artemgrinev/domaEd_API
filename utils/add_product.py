import asyncio
from elasticsearch import AsyncElasticsearch, RequestError
from db.elasticsearch.maps import MAPPING_FOR_PRODUCT
from utils.products import product_list


async def main():
    elastic_client = AsyncElasticsearch('http://localhost:9200')
    try:
        await elastic_client.indices.create(index="products", mappings=MAPPING_FOR_PRODUCT)
    except RequestError as err:
        print(err)
    for document in product_list:
        await elastic_client.index(index="products", document=document)


if __name__ == "__main__":
    asyncio.run(main())
