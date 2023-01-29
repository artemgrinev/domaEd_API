MAPPING_FOR_PRODUCT = {
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
                "product_id": {
                    "type": "integer"
                },
                "category": {
                    "type": "text",
                    "analyzer": "russian",
                    "fields": {
                        "keyword": {
                            "type": "keyword"
                        }
                    }
                },
                "manufacturer": {
                    "type": "text",
                    "analyzer": "russian",
                    "fields": {
                        "keyword": {
                            "type": "keyword"
                        }
                    }
                },
                "price": {
                    "type": "float"
                },
                "amount": {
                    "type": "float"
                },
                "measure": {
                    "type": "text"
                },
                "update_date": {
                    "type": "date"
                },
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
