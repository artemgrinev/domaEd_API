import datetime
from elasticsearch import NotFoundError, Elasticsearch, RequestError, AsyncElasticsearch


class Indexer(object):
    def __init__(self, ec: AsyncElasticsearch,
                 products: list, index_alias: str, mappings: dict):
        self.elastic_client = ec
        self.products = products
        self.index_alias = index_alias
        self.mappings = mappings

    # def build_new_index(self) -> str:
    #     index_name = "products-" + datetime.datetime.now().strftime("%Y-%m-%d")
    #     self.create_empty_index(index_name)
    #     for product in self.products:
    #         self.put_card_into_index(product, index_name)
    #     return index_name

    async def build_new_index(self):
        index_name = "products-" + datetime.datetime.now().strftime("%Y-%m-%d")
        try:
            await self.create_empty_index(index_name)
        except RequestError as err:
            print(err)
        for document in self.products:
            await self.put_card_into_index(document, index_name)
        return index_name

    async def create_empty_index(self, index_name: str):
        try:
            await self.elastic_client.indices.create(index=index_name, mappings=self.mappings)
        except RequestError as err:
            print(err)

    async def put_card_into_index(self, product, index_name: str):
        await self.elastic_client.create(index=index_name, document=product)

    def switch_current_index(self, new_index_name: str):
        try:
            remove_actions = [
                {
                    "remove": {
                        "index": index_name,
                        "alias": self.index_alias,
                    }
                }
                for index_name in self.elastic_client.indices.get_alias(name=self.index_alias)
            ]
        except NotFoundError:
            remove_actions = []

        self.elastic_client.indices.update_aliases({
            "actions": remove_actions + [dict(add=dict(index=new_index_name, alias=self.index_alias))]
        })
