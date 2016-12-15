import logging

import grab

from . import celery
from . import parser


logger = logging.getLogger(__name__)

task = celery.app.task


@task
def process_url(url):
    logger.info('Processing %s...' % url)

    g = grab.Grab()
    resp = g.go(url)

    for found_url in parser.parse_urls(resp.body.decode()):
        logger.info('Found URL: %s' % found_url)
