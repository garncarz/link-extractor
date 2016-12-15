from extractor import parser


def test_parse_urls():
    links = [
        'https://docs.python.org/3/library/re.html#re.compile',
        'https://vietcong1.eu/cs/game/players#playersList-perPage=100'
            '&playersList-sort[onlineSince]=asc',
        'http://deviantart.com',
        'https://www.google.cz/search?q=umbrella&oq=umbrella'
            '&aqs=chrome..69i57j0l5.19399j0j7&sourceid=chrome&ie=UTF-8',
    ]
    text = '''
    <html>
        <body>
            <a href="{}">link</a>
            {}
            <ul>
                <li>{}
            </ul>
            - {}
        </body>
    </html>
    '''.format(*links)

    found = list(parser.parse_urls(text))

    assert len(links) == len(found)

    for url1, url2 in zip(links, found):
        assert url1 == url2
