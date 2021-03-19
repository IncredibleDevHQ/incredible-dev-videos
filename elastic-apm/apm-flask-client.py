import os
from flask import Flask
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.contrib.flask import ElasticAPM

flask_app = Flask(__name__)
flask_app.config['ELASTIC_APM'] = {
  'SERVICE_NAME': 'Incredible_APM',
  'SECRET_TOKEN': os.getenv('SECRET_TOKEN'),
  'SERVER_URL': os.getenv('SERVER_URL'),
}
apm_client = ElasticAPM(flask_app,logging=True)

@flask_app.route("/")
def foo():
    try:
        1 / 0
    except ZeroDivisionError:
        apm_client.capture_exception()

if __name__ == "__main__":
    flask_app.run(debug=False,port=6060)
