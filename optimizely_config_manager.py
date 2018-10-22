import requests
from optimizely import optimizely
from optimizely.logger import SimpleLogger

class OptimizelyConfigManager(object):
  """A simple class for managing the optimizely instance."""

  def __init__(self, sdk_key):
    """Initialize a OptimizelyConfigManager object."""
    self.sdk_key = sdk_key
    self.instance = None

  def get_instance(self):
    """Return the Optimizely instance, initializing it if needed."""
    if not self.instance:
      self.set_instance()
    return self.instance

  def set_instance(self):
    """Initializing the Optimizely instance."""
    datafile = ''
    if self.sdk_key is None:
      datafile=open('datafile.json', 'r').read()
    else:
      url = 'https://cdn.optimizely.com/datafiles/{0}.json'.format(self.sdk_key)
      datafile = requests.get(url).text

    self.instance = optimizely.Optimizely(datafile, None, SimpleLogger())
    return datafile