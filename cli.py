import argparse


class CLI:
    """ Command line interface for GitLab Group Backup """

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self._setup()

    def _setup(self):
        self.parser.add_argument("-u", "--gitlab-url", required=True, help="URL of the GitLab instance to access")
        self.parser.add_argument("-t", "--access-token", required=False, help="GitLab API access token")
        self.parser.add_argument("-p", "--path", default="/", required=False, help="Limit backed up elements to given path (e.g. '/username/group')")

    def parse_args(self):
        """
        Parses CLI arguments

        :return dict containing CLI arguments
        """
        return vars(self.parser.parse_args())
