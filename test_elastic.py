from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch('http://localhost:9200')

# doc = {
#     'author': 'kimchy',
#     'text': 'Говядина грудинка',
#     'timestamp': datetime.now(),
# }
# resp = es.index(index="test-index", id=2, document=doc)
# print(resp['result'])
#
# resp = es.get(index="test-index", id=2)
# print(resp['_source'])
#
# es.indices.refresh(index="test-index")

resp = es.search(index="test-index", query={"match": {"text":"Говяжья грудинка"}})
print(resp)
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])