[![Build Status](https://travis-ci.org/garncarz/link-extractor.svg?branch=master)](https://travis-ci.org/garncarz/link-extractor)
[![Coverage Status](https://coveralls.io/repos/github/garncarz/link-extractor/badge.svg?branch=master)](https://coveralls.io/github/garncarz/link-extractor?branch=master)


## Installation

Needed:
- Python 3.5
- Redis

Preferably under `virtualenv`:

`pip install pip-tools` (once)

`pip-sync requirements*.txt` (keeping the PyPI dependencies up-to-date)


## Configuration

Customized settings are expected in `extractor/settings_local.py`.
(But they shouldn't be needed.)


## Usage

`redis-server redis.conf`

`celery -A extractor worker -l info`


## Testing

`./test.sh` (also generates a coverage)
