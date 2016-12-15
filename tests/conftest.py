import shutil
import tempfile

import pytest

from extractor import settings


@pytest.yield_fixture(autouse=True)
def tmp_out():
    settings.OUT_DIR = tempfile.mkdtemp()
    yield
    shutil.rmtree(settings.OUT_DIR)
