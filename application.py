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

PORT = 4001

##
# Optimizely element masking
##

# Optimizely Project IDs
FULL_STACK_PROJECT_ID = '11105544875'
WEB_PROJECT_ID = '11085868647'

# Full Stack feature/variable keys
GLOBAL_CONFIG = 'global_config'
MASK_TIMEOUT = 'mask_timeout'
MASK_TIMEOUT_TYPE = 'integer'
IS_SNIPPET_SYNCHRONOUS = 'is_snippet_synchronous'
IS_SNIPPET_SYNCHRONOUS_TYPE = 'boolean'
CSS_SELECTOR = 'css_selector'
CSS_SELECTOR_TYPE = 'string'


# None of the masking logic is user-specific in this example, so we keep the user_id constant
USER_ID = ''

# Initialization
config_manager = OptimizelyConfigManager(FULL_STACK_PROJECT_ID)
application = Flask(__name__, static_folder='images')
application.secret_key = os.urandom(24)

def get_mask_timeout():
  """Retrieve the mask timeout value from the global config feature."""
  timeout = config_manager.get_variable(GLOBAL_CONFIG, MASK_TIMEOUT, USER_ID, MASK_TIMEOUT_TYPE)
  if timeout is None:
    timeout = 0
  return timeout

def get_is_snippet_synchronous():
  return config_manager.get_variable(GLOBAL_CONFIG, 
                                     IS_SNIPPET_SYNCHRONOUS, 
                                     USER_ID, 
                                     IS_SNIPPET_SYNCHRONOUS_TYPE)

def get_masked_elements():
  """Retrieve the list of masked element css selectors from the active Full Stack Features."""
  features = config_manager.get_enabled_features(USER_ID)
  masked_elements = []
  for feature in features:
    if feature != GLOBAL_CONFIG:
      css_selector = config_manager.get_variable(feature, CSS_SELECTOR, USER_ID, CSS_SELECTOR_TYPE)
      if css_selector:
        masked_elements.append(css_selector)
  return masked_elements

##
# Request Handlers
##

# render homepage
@application.route('/')
def index():
  """Request handler for '/'; renders templates/index.html."""
  return render_template('index.html', 
                         is_snippet_synchronous=get_is_snippet_synchronous(),
                         masked_elements=get_masked_elements(),
                         web_project_id=WEB_PROJECT_ID,
                         mask_timeout = get_mask_timeout())

# render homepage
@application.route('/refresh')
def refresh_datafile():
  """Request handler for '/refresh'; used to manually trigger a datafile refresh."""
  datafile = config_manager.set_obj()
  return datafile, 200, {'ContentType':'application/json'} 

##
# Main
##

if __name__ == '__main__':
  application.debug = True
  application.run(port=PORT)
