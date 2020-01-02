# Simple producer/consumer web link extractor

[![Build Status](https://travis-ci.org/garncarz/link-extractor.svg?branch=master)](https://travis-ci.org/garncarz/link-extractor)
[![Coverage Status](https://coveralls.io/repos/github/garncarz/link-extractor/badge.svg?branch=master)](https://coveralls.io/github/garncarz/link-extractor?branch=master)


## Installation

Needed:
- Python 3.5
- Redis
- Supervisord

Preferably under `virtualenv`:

`pip install pip-tools` (once)

`pip-sync requirements*.txt` (keeping the PyPI dependencies up-to-date)


## Configuration

Customized settings are expected in `extractor/settings_local.py`.
(But they shouldn't be needed.)


## Usage

`supervisord` starts Supervisord with background services
(Redis, Celery workers – "consumers").
They can be controlled by `supervisorctl` then.
Logs are stored in the `log` directory.

`./app.py` is the "producer", expecting list of URLs on the standard input.
They are parsed, so you can use HTML as input: `./app.py < index.html`.

Each URL from input is processed by consumers in a way that
the referenced webpage is downloaded and parsed for absolute URLs,
which are then saved in a JSON file in the `out` directory.
The output file name is an MD5 hash of the input URL.


## Example

```sh
$ supervisord  # if not already done before
$ ./app.py
http://example.com
Ctrl+D
$ jq < out/a9b9f04336ce0181a08e774e01113b31.json
{
  "url": "http://example.com",
  "links": [
    "http://www.iana.org/domains/example"
  ],
  "version": "0.1.0"
}
```


## Testing

`./test.sh` (also generates a coverage)


<!-- ❄️ Hello to the GitHub Archive! ❄️ -->
