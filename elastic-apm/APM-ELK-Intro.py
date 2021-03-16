# APM = Application Performance Monitoring
# > collect data about incoming requests and background tasks
# > collect data from database drivers, HTTP libraries etc
# > collect system and application metrics in regular intervals

# Components of APM!
# APM Agent -> APM Server -> Elastic Search  -> Kibana APM UI

# Link in description (Read more at ): https://www.elastic.co/guide/en/apm/get-started/current/components.html

# Go to the link in the description and follow STEP-1 url(https://www.elastic.co/guide/en/apm/get-started/current/install-and-run.html).
# Make sure you have the below details before proceeding :
# export USER=elastic
# export PASSWORD=uX6W49ItIRQUPMCj4xi1OqCN
# export ENDPOINT=https://fdd712011b134f6bab2461ef7c134789.apm.us-central1.gcp.cloud.es.io
# export SECRET_TOKEN=D6Eb1eFTtWPjGv6CKR

# Client Installtion: $ pip install elastic-apm[flask]