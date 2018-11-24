class Configuration(object):
    """ Loads and stores a configuration file or buffer """

    def __init__(self, filename=None):
        self.filename = filename

    def load(self):
        """ Given the filename, loads the configuration into the class """
        success = False

        if filename is not None:
            with open(filename, 'r') as config_file:
                success = True

        return success
