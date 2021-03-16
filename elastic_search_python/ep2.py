from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

tweet = {
    'author': 'IncredbleDevHQ',
    'text': 'Signup for beta on incredible.dev',
    'timestamp': datetime.now(),
}

es.indices.create(index='es-intro',ignore=[400])
res = es.index(index="es-intro", id=1, body=tweet)
print(res['result'])
# response : updated

res = es.get(index="es-intro", id=1)
print(res['_source'])
# respone : {'author': 'IncredbleDevHQ', 'text': 'Signup for beta on incredible.dev', 'timestamp': '2021-03-15T19:13:13.764680'}

es.indices.refresh(index="es-intro")

res = es.search(index="es-intro", body={"query": {"match_all": {}}})

for hit in res['hits']['hits']:
    print(f'{hit["_source"]}')