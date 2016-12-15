import json
import os
from unittest.mock import patch, MagicMock

from extractor import io, settings, tasks


@patch('grab.Grab.go')
def test_process_url(grab_go):
    url = 'http://example.com'
    links = [
        'https://first.com',
        'http://second.eu/?q=foo',
    ]
    text = '''
    <a href="{}">lnk</a>
    {}
    '''.format(*links)

    grab_go.side_effect = MagicMock(
        return_value=MagicMock(
            body=text.encode(),
        ),
    )

    tasks.process_url(url)

    assert grab_go.call_args[0][0] == url

    with open(os.path.join(settings.OUT_DIR, io.hash_name(url) + '.json')) \
            as f:
        data = json.loads(f.read())

    assert data['url'] == url
    assert data['links'] == links
