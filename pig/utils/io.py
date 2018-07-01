import os

class Io:

  @classmethod
  def createFolders(self, directory):
    if not os.path.exists(directory):
      os.makedirs(directory)