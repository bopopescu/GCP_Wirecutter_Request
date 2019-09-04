from urllib3 import PoolManager
from urllib3.contrib.appengine import AppEngineManager, is_appengine_sandbox
from flask import Flask
import requests
import requests_toolbelt.adapters.appengine

requests_toolbelt.adapters.appengine.monkeypatch()

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://storage.googleapis.com/nyt-ads-static-assets/ads/adplatforms/HD_Source_150080.json'

    if is_appengine_sandbox():
        http = AppEngineManager()
    else:
        http = PoolManager()

     resp = http.request('GET', url)

     return resp.data	


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
        return """
    An internal error occurred: <pre>{}</pre>
    ee logs for full stacktrace.
     """.format(e), 500