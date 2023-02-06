product_synonyms_list = ["говяжий, говядина"]

settings = {
    "number_of_shards": 2,
    "number_of_replicas": 1,
    "analysis": {
        "analyzer": {
            "rus_analyzer": {
                "type": "custom",
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "rus_analyzer_filter",
                    "synonym_filter"
                ]
            }
        },
        "filter": {
            "rus_analyzer_filter": {
                "type": "hunspell",
                "locale": "ru_RU",
                "dedup": True
            },
            "synonym_filter": {
                "type": "synonym_graph",
                "synonyms": product_synonyms_list
            }
        }
    }
}
product_mappings = {
    "dynamic": "true",
    "numeric_detection": "true",
    "_source": {
      "enabled": "true"
    },
    "properties": {
        "amount": {
            "type": "float"
        },
        "category": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            },
            "analyzer": "rus_analyzer"
        },
        "manufacturer": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            },
            "analyzer": "rus_analyzer"
        },
        "market_name": {
            "type": "text"
        },
        "measure": {
            "type": "text"
        },
        "name": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            },
            "analyzer": "rus_analyzer"
        },
        "price": {
            "type": "float"
        },
        "product_id": {
            "type": "long",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "product_url": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "update_date": {
            "type": "date"
        }
    }
}
