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