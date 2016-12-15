#!/usr/bin/env python3

import sys

from extractor import parser, tasks


def main():
    for url in parser.parse_urls(sys.stdin.read()):
        tasks.process_url.delay(url)


if __name__ == '__main__':
    main()
