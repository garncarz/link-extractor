import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Celery

BROKER_URL = 'redis+socket://%s/redis.sock' % BASE_DIR


try:
    from .settings_local import *
except ImportError:
    pass
