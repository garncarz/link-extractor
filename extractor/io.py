import hashlib
import json
import logging
import os

from . import __version__
from . import settings


logger = logging.getLogger(__name__)


def hash_name(name):
    return hashlib.md5(name.encode()).hexdigest()


def save_links(url, links):
    data = {
        'url': url,
        'links': links,
        'version': __version__,
    }

    filename = os.path.join(settings.OUT_DIR, hash_name(url) + '.json')
    with open(filename, 'w') as f:
        f.write(json.dumps(data))

    logger.info('Links for %s saved into %s' % (url, filename))
