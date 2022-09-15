# MIT License
#
# Copyright (c) 2022 Niels Gandraß <niels@gandrass.de>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
