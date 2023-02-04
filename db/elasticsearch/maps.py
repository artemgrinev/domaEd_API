product_synonyms_list = ["говяжий, говядина"]

ANALYZER = {
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
                    "synonyms": ["говяжий, говядина"]
                }
            }
        }
    }

MAPPING_FOR_RECIPES = {
    "properties": {
        "name": {
            "type": "text",
            "analyzer": "russian",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "resource": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            }
        },
        "url": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword"
                }
            },
        },
        "update_date": {
            "type": "date"
        },
        "ingredients": [
            {"name": "text",
             "price": "float",
             "measure": ""},
        ]
    }
}

MAPPING_FOR_PRODUCT = {
    "mappings": {
        "properties": {
            "name": {
                "type": "text",
                "analyzer": "rus_analyzer",
                "fields": {
                    "keyword": {
                        "type": "keyword"
                    }
                }
            },
            "category": {
                "type": "text"
            },
            "market_name": {
                "type": "text"
            },
            "product_url": {
                "type": "text"
            },
            "product_id": {
                "type": "text"
            },
            "price": {
                "type": "text"
            },
            "manufacturer": {
                "type": "text"
            },
            "amount": {
                "type": "text"
            },
            "measure": {
                "type": "text"
            },
            "update_date": {
                "type": "date"
            }
        }
    },
    "settings": ANALYZER
}
