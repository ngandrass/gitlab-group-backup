import argparse


class CLI:
    """ Command line interface for GitLab Group Backup """

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self._setup()

    def _setup(self):
        self.parser.add_argument("-u", "--gitlab-url", type=str, required=True, help="URL of the GitLab instance to access")
        self.parser.add_argument("-g", "--group-id", type=int, required=True, help="ID of the root group to backup")
        self.parser.add_argument("-t", "--access-token", type=str, required=False, help="GitLab API access token")

    def parse_args(self):
        """
        Parses CLI arguments

        :return dict containing CLI arguments
        """
        return vars(self.parser.parse_args())
