from elasticsearch import Elasticsearch
from db.elasticsearch.maps import MAPPING_FOR_PRODUCT
from utils.index_builder import Indexer
from utils.products import product_list

host = 'http://localhost:9200'
elastic_client = Elasticsearch(host)


def index(indexer: Indexer):
    new_index_name = indexer.build_new_index()
    indexer.switch_current_index(new_index_name)


if __name__ == "__main__":
    indexer = Indexer(elastic_client, product_list, "products", MAPPING_FOR_PRODUCT)
    index(indexer)
