import os
from flask import Flask
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.handlers.logging import LogginHandler

app = Flask(__name__)
apm = ElasticAPM(app)

@app.route("/")
def bar():
    try:
        1 / 0
    except ZeroDivisionError:
        app.logger.error('I cannot math',exec_info=True)
        
if __name__ == "__main__":
    handler = LoggingHandler(client=apm.client)
    handler.setLevel(logging.WARM)
    app.logger.addHandler(handler)
