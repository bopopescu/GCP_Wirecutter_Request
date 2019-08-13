  
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging

from flask import Flask

# [START imports]
import requests
import requests_toolbelt.adapters.appengine

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()
# [END imports]

app = Flask(__name__)


@app.route('/')
def index():
    # [START requests_get]
    url = 'https://storage.googleapis.com/nyt-ads-static-assets/ads/adplatforms/HD_Source_150080.json'
    response = requests.get(url)
    response.raise_for_status()
    return response.text
    # [END requests_get]


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500
# [END app]




# Error - file: 'file:///Users/208414/Desktop/GithubRepos/GCP_Wirecutter_Request/GCP_App_Engine/python-docs-samples/appengine/standard_python37/hello_world/main.py'
# severity: 'Error'
# message: 'E0401:Unable to import 'requests_toolbelt.adapters.appengine''
# at: '23,1'
# source: 'pylint'