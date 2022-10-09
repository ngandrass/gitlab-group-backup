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

import argparse


class CLI:
    """
    Command line interface for GitLab Group Backup
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self._setup()

    def _setup(self) -> None:
        self.parser.add_argument("-u", "--gitlab-url",
            type=str,
            required=True,
            help="URL of the GitLab instance to access"
        )

        self.parser.add_argument("-g", "--group-id",
            type=int,
            required=True,
            help="ID of the root group to backup"
        )

        self.parser.add_argument("-t", "--access-token",
            type=str,
            required=False,
            default=None,
            help="GitLab API access token"
        )

        self.parser.add_argument("-o", "--output-dir",
            type=str,
            required=False,
            default="out",
            help="Directory to write GitLab exports into"
        )

        self.parser.add_argument("-s", "--create-subdir",
            action="store_true",
            required=False,
            default=False,
            help="Create a new subdirectory, named by backup date, inside output directory for each backup"
        )

    def parse_args(self) -> dict:
        """
        Parses CLI arguments

        :return dict containing CLI arguments
        """
        return vars(self.parser.parse_args())
