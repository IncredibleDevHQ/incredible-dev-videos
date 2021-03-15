import elasticsearch
es = elasticsearch.Elasticsearch(HOST="http://localhost",PORT=9200)

# Let's create an index
es.indices.create(index='es-intro',ignore=[400])
# response: {'acknowledged': True, 'shards_acknowledged': True, 'index': 'es-intro'}

# Delete an index 
es.indices.delete(index="es-intro",ignore=[400,404])
# response {'acknowledged': True}

# Check if the index was deleted
es.indices.exists(index="es-intro")
# response: False/True
