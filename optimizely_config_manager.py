import requests
from optimizely import optimizely
from optimizely.logger import SimpleLogger

class OptimizelyConfigManager(object):
  """A simple class for managing the optimizely instance."""

  def __init__(self, sdk_key):
    """Initialize a OptimizelyConfigManager object."""
    self.sdk_key = sdk_key
    self.instance = None
    self.datafile = None

  def get_instance(self):
    """Return the Optimizely instance, initializing it if needed."""
    if not self.instance:
      self.set_instance()
    return self.instance

  def set_instance(self):
    """Initializing the Optimizely instance."""
    if self.sdk_key is None:
      self.datafile=open('datafile.json', 'r').read()
    else:
      url = 'https://cdn.optimizely.com/datafiles/{0}.json'.format(self.sdk_key)
      self.datafile = requests.get(url).text

    self.instance = optimizely.Optimizely(self.datafile, None, SimpleLogger())
    return self.datafile

  def get_datafile(self):
    """Return the current datafile"""
    if not self.instance:
      self.set_instance()
    return self.datafile