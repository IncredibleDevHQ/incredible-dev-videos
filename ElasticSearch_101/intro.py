# Elastic Search
# Super Easy Installation -> $ pip install elastic-apm[flask]
from flask import Flask

from elasticapm.contrib.flask import ElasticAPM
from elasticapm.handlers.logging import LoggingHandler

app = Flask(__name__)

apm = ElasticAPM(app)

if __name__ == '__main__':
    # Create a logging handler and attach it.
    handler = LoggingHandler(client=apm.client)
    handler.setLevel(logging.WARN)
    app.logger.addHandler(handler)

@app.route('/')
def bar():
    try:
        1 / 0
    except ZeroDivisionError:
        app.logger.error( 'I cannot math', exc_info=True)
