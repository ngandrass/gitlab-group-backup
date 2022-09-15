# GitLab Group Backup

Uses the GitLab API to create backups of a group including its subgroups and all projects.

For usage information see: `./main.py -h`

If your group is private a group access token with the following permissions is required:
  - Role: Owner
  - Scopes: `api`, `read_api`, `read_repository`

The token can be supplied via the `--access-token` CLI option.


## Notes

 - Request rate limiting is automatically applied