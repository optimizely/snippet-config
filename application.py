# Python SDK Demo App
# Copyright 2016 Optimizely. Licensed under the Apache License
# View the documentation: http://optimize.ly/py-sdk 
from __future__ import print_function

import csv
import json
import os
from operator import itemgetter
from optimizely_config_manager import OptimizelyConfigManager
from flask import Flask, render_template, request

##
# Globals
##

PORT = 4001

# Optimizely Full Stack SDK Key (use None in order to read from local filesystem)
SNIPPET_CONFIG_FULL_STACK_SDK_KEY = None 

# For simplicity, we use a blank user_id value
USER_ID = ''


##
# Initialization
##

config_manager = OptimizelyConfigManager(SNIPPET_CONFIG_FULL_STACK_SDK_KEY)
application = Flask(__name__, static_folder='images')
application.secret_key = os.urandom(24)



##
# Request Handlers
##

# render homepage
@application.route('/')
def index():
  """Request handler for '/'; renders templates/index.html."""
  optimizely_client = config_manager.get_instance()
  return render_template('index.html',
    is_snippet_enabled=optimizely_client.is_feature_enabled('snippet_config', 
                                                            USER_ID),
    is_snippet_synchronous=optimizely_client.get_feature_variable_boolean('snippet_config', 
                                                                          'is_snippet_synchronous', 
                                                                          USER_ID),
    snippet_url=optimizely_client.get_feature_variable_string('snippet_config', 
                                                              'snippet_url', 
                                                              USER_ID), 
    datafile=config_manager.get_datafile())
 
# render homepage
@application.route('/refresh')
def refresh_datafile():
  """Request handler for '/refresh'; used to manually trigger a datafile refresh."""
  datafile = config_manager.set_instance()
  return datafile, 200, {'ContentType':'application/json'} 


##
# Main
##

if __name__ == '__main__':
  application.debug = True
  application.run(port=PORT)
