import datetime
from elasticsearch import RequestError, Elasticsearch, AsyncElasticsearch


class Builder(object):
    def __init__(self, host, name: str,
                 document: list, mappings: dict, settings: dict):
        self.index_name = name
        self.elastic_client = Elasticsearch(host)
        self.async_elastic_client = AsyncElasticsearch(host)
        self.document = document
        self.mappings = mappings
        self.settings = settings

    async def build_new_index(self, index_name):
        for doc in self.document[:10]:
            print(f'id: {doc["id"]} nam: {doc["card"]["name"]}')
            await self.put_card_into_index(doc["card"], index_name)

    def create_empty_index(self):
        index_name = self.index_name + datetime.datetime.now().strftime("%Y-%m-%d")
        try:
            self.elastic_client.indices.create(index=index_name,
                                               mappings=self.mappings,
                                               settings=self.settings)
            print(f"created new index: {index_name}")
        except RequestError as err:
            print(err)
        finally:
            return index_name

    async def put_card_into_index(self, product, index_name: str):
        try:
            await self.async_elastic_client.index(index=index_name, document=product)
        except Exception as ex:
            print(str(ex))

