import yaml


class Config:
    """ Config class for GitLab Group Backup """

    CONFIG_FILE = "config.yaml"
    CONFIG = {}

    def __init__(self):
        return

    def get(self, key):
        return self.CONFIG[key]

    def set(self, key, value):
        self.CONFIG[key] = value

    def parse_config_file(self):
        """ Parses the config file from disk and loads its values """
        with open(self.CONFIG_FILE) as f:
            self.add_config_values(yaml.load(f, Loader=yaml.loader.SafeLoader))

    def add_config_values(self, new_values: dict):
        """ Extends this Config object by the given key-value pairs """
        if new_values is None:
            return

        self.CONFIG = dict(self.CONFIG, **new_values)
