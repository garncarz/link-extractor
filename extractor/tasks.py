import logging

from . import celery


logger = logging.getLogger(__name__)

task = celery.app.task


@task
def process_url(url):
    logger.info('Processing %s...' % url)
