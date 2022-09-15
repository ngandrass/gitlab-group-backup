#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
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

from datetime import datetime
import logging
import os
import time

import gitlab

from cli import CLI
from config import Config

CLI = CLI()
CFG = Config()
LOG = logging.getLogger(__name__)


class GitLabGroupBackup:

    def __init__(self):
        self.GitLab = None
        self.date_str = datetime.today().strftime('%Y-%m-%d_%H%M%S')

    def main(self):
        CFG.add_config_values(CLI.parse_args())
        CFG.parse_config_file()

        logging.basicConfig(encoding="utf-8", level=CFG.get("loglevel"))
        LOG.debug(f"Config: {CFG.CONFIG}")

        # Authenticate at GitLab API
        self.GitLab = gitlab.Gitlab(url=CFG.get("gitlab_url"), private_token=CFG.get('access_token'))
        self.GitLab.auth()

        # Get root group and all subgroups from API
        root_group = self.GitLab.groups.get(CFG.get("group_id"))
        LOG.debug(f"Root group: {root_group}")
        LOG.info(f"Found root group: {root_group.full_name} (ID: {root_group.id}) - {root_group.web_url}")

        LOG.info(f"Querying subgroups ...")
        subgroups = []
        for subgroup in root_group.descendant_groups.list():
            subgroups.append(self.GitLab.groups.get(subgroup.id))

        # Backup groups
        for group in [root_group] + subgroups:
            self._backup_group(group)

    def _backup_group(self, group):
        """ Creates a backup of a given group and triggers backups of all contained projects """
        # Create backup target
        LOG.info(f"vvv Starting backup of group: {group.full_name} (ID: {group.id}) - {group.web_url} vvv")
        filestore_path = os.path.join(CFG.get('output_dir'), group.full_path)
        os.makedirs(filestore_path, exist_ok=True)

        # Export group settings
        export = group.exports.create()
        time.sleep(CFG.get('group_backup_backoff_sec'))
        backup_file = os.path.join(filestore_path, f"group_{group.path}_{group.id}_{self.date_str}.tar.gz")
        with open(backup_file, 'wb') as f:
            LOG.info(f"Export finished. Writing group backup to: {backup_file}")
            export.download(streamed=True, action=f.write)

        # Backup group projects
        for project in group.projects.list():
            self._backup_project(self.GitLab.projects.get(project.id), filestore_path)

        LOG.info(f"^^^ Finished processing of group: {group.full_name} (ID: {group.id}) - {group.web_url} ^^^")

    def _backup_project(self, project, target_dir):
        """ Creates a backup of the given project """
        # Trigger export routine
        LOG.info(f"Backing up project: {project.name} (ID: {project.id}) - {project.web_url}")
        export = project.exports.create()

        # Wait for export to finish
        export.refresh()
        while export.export_status != 'finished':
            time.sleep(1)
            export.refresh()

        # Download the exported archive
        backup_file = os.path.join(target_dir, f"{project.path}_{project.id}_{self.date_str}.tar.gz")
        with open(backup_file, 'wb') as f:
            LOG.info(f"Export finished. Writing project backup to: {backup_file}")
            export.download(streamed=True, action=f.write)


if __name__ == "__main__":
    GLGB = GitLabGroupBackup()
    GLGB.main()
