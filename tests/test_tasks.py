from unittest.mock import patch, MagicMock

from extractor import tasks


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
