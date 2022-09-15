# GitLab Group Backup

Uses the GitLab API to create backups of a group including its subgroups and all projects.

Usage example: `./main.py --gitlab-url=https://gitlab.com --access-token=0123456789ABCDEF --group-id=42`

For detailed information see: `./main.py -h`

If your group is private a group access token with the following permissions is required:
  - Role: Owner
  - Scopes: `api`, `read_api`, `read_repository`

The token can be supplied via the `--access-token` CLI option.


## Requirements

All requirements are managed by [poetry](https://python-poetry.org/). It must therefore be installed on the system.


## Installation

To install all software requirements run `poetry install` inside the project root directory.


## Configuration

This tool is primarily configured by CLI arguments (see: `./main.py -h`). The `config.yaml` file contains additional
configuration parameters and can be used to overwrite any of the CLI arguments.


## Running via Docker

To run this tool using Docker, conduct the following steps:

  1. Copy `.env.dist` to `.env` and add your configuration details
  2. Build the image: `docker compose build`
  3. Run a container: `docker compose run gitlab-group-backup`

Exports are written into the `/data` folder inside the container. It is mapped to the host folder `./data` by default.


## Notes

  - Request rate limiting is automatically applied. A strongly enforced rate limit can greatly impact the execution time
    of this script.
  - The `Owner` role and `api` scope are required to allow creation of backups inside GitLab.
