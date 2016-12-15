import re


re_urls = re.compile(r'(?P<url>https?://[^\s"]+)')


def parse_urls(text):
    for match in re_urls.finditer(text):
        yield match.group('url')
