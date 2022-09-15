#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

import gitlab

from cli import CLI
from config import Config

CLI = CLI()
CFG = Config()
GITLAB = gitlab.Gitlab()
LOG = logging.getLogger(__name__)

class GitLabGroupBackup:

    def __init__(self):
        pass

    def main(self):
        CFG.add_config_values(CLI.parse_args())
        CFG.parse_config_file()

        logging.basicConfig(encoding="utf-8", level=CFG.get("loglevel"))
        LOG.debug(f"Config: {CFG.CONFIG}")


if __name__ == "__main__":
    GLGB = GitLabGroupBackup()
    GLGB.main()
