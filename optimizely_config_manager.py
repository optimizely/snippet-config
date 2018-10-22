import requests
from optimizely import optimizely
from optimizely.logger import SimpleLogger

class OptimizelyConfigManager(object):

  VARIABLE_GETTERS = {
    'string' : optimizely.Optimizely.get_feature_variable_string,
    'boolean' : optimizely.Optimizely.get_feature_variable_boolean,
    'double' : optimizely.Optimizely.get_feature_variable_double,
    'integer' : optimizely.Optimizely.get_feature_variable_integer
  }

  def __init__(self, project_id):
    self.project_id = project_id
    self.obj = None

  def get_obj(self):
    if not self.obj:
      self.set_obj()
    return self.obj

  def set_obj(self, url=None):
    if not url:
      url = 'https://cdn.optimizely.com/json/{0}.json'.format(self.project_id)

    datafile = self.retrieve_datafile(url)
    self.obj = optimizely.Optimizely(datafile, None, SimpleLogger())
    return datafile

  def retrieve_datafile(self, url):
    datafile = requests.get(url).text
    return datafile

  def get_variable(self, feature, variable, user, type='string'):
    if type not in OptimizelyConfigManager.VARIABLE_GETTERS:
      return None
    getter = OptimizelyConfigManager.VARIABLE_GETTERS[type]
    return getter(self.get_obj(), feature, variable, user)

  def get_enabled_features(self, user):
    return self.get_obj().get_enabled_features(user)

