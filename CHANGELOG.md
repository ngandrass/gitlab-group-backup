# Version 1.4.0 (2023-02-28)

  - Retry exporting GitLab objects for `export_retry_count` times before exiting with error.
  - Update external libraries

# Version 1.3.0 (2023-01-26)

  - Fetch all groups and projects without upper limit
  - Update external libraries

# Version 1.2.0 (2022-10-09)

  - Allow backup of multiple groups at the same time
    - The `-g`/`--group-id` CLI argument can be repeated to backup multiple groups within a single run.
      Example: `./main.py --gitlab-url=https://gitlab.com --access-token=0123456789ABCDEF --group-id=42 --group-id=1337`

# Version 1.1.1 (2022-10-09)

  - Improve error reporting
  - Update python dependencies
  - Improve documentation


# Version 1.1.0 (2022-10-09)

Initial stable public release