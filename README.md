# GitLab Group Backup

Creates full backups of a GitLab group including its subgroups and all projects via the GitLab API.

  - Separate backup archives for group metadata and projects
  - One backup file per repository, allowing selective restoring via the GitLab web interface or API
  - Repositories are stores as [git bundles](https://git-scm.com/docs/git-bundle), allowing to restore data independent
    of GitLab.
  - Handles rate-limiting of GitLab API
  - Can automatically be run as recurring task via Docker

## Usage

Usage example: `./main.py --gitlab-url=https://gitlab.com --access-token=0123456789ABCDEF --group-id=42`

```text
usage: main.py [-h] [-s] -u GITLAB_URL -g GROUP_ID [-t ACCESS_TOKEN]
               [-o OUTPUT_DIR]

options:
  -h, --help            show this help message and exit
  -s, --create-subdir   Create a new subdirectory, named by backup date,
                        inside output directory for each backup
  -u GITLAB_URL, --gitlab-url GITLAB_URL
                        URL of the GitLab instance to access
  -g GROUP_ID, --group-id GROUP_ID
                        ID of the root group to backup
  -t ACCESS_TOKEN, --access-token ACCESS_TOKEN
                        GitLab API access token
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Directory to write GitLab exports into

```

See also: `./main.py -h`


## Requirements

All software dependencies are managed via [poetry](https://python-poetry.org/). It must therefore be installed on the
system. This project heavily relies on the [python-gitlab](https://github.com/python-gitlab/python-gitlab) project,
check them out :)


## Installation

To install all software dependencies run `poetry install` inside the project root directory.


## Configuration

This tool is primarily configured by CLI arguments (see: `./main.py -h`). The `config.yaml` file contains additional
configuration parameters and can be used to overwrite any of the CLI arguments.

### Private Groups / Access Token Scopes

If your group is private, a group access token with the following permissions is required:
  - Role: Owner
  - Scopes: `api`, `read_api`, `read_repository`

The token can be supplied via the `--access-token` CLI option or via the `config.yaml` file.


## Running via Docker

A `docker-compose.yaml` file is provided. To run this tool using Docker, conduct the following steps:

  1. Copy `.env.dist` to `.env` and add your configuration details
  2. Build the image: `docker compose build`
  3. Run a container: `docker compose run gitlab-group-backup`

Exports are written into the `/data` folder inside the container. It is mapped to the host folder `./data` by default.


## Notes

  - Request rate limiting is automatically applied. A strongly enforced rate limit can greatly impact the execution time
    of this script.
  - The `Owner` role and `api` scope are required to allow creation of backups inside GitLab.
