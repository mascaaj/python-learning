"""
pick a start website
go thru html code
    based on regex find html tags
    add to adjacency matrix ? or queue ?
dequeue, perfom same action recursively
"""

import requests
import re


class WebCrawler:

    def __init__(self):
        self.discovered_websites = []

    def crawl(self, start_url):
        """
        steps
            start at a url in queue
            get url, pop
            get html
            for valid urls in parsed html
                if url is not in discovered websites
                append to queue
        """
        queue = [start_url]
        self.discovered_websites.append(start_url)

        while queue:
            actual_url = queue.pop(0)
            print(actual_url)

            actual_url_html = self.read_raw_html(actual_url)
            for url in self.get_links_from_html(actual_url_html):
                if url not in self.discovered_websites:
                    self.discovered_websites.append(url)
                    queue.append(url)

    def read_raw_html(self, url):
        raw_html = ''
        try:
            raw_html = requests.get(url).text
        except Exception as e:
            print(e)
            pass

        return raw_html

    def get_links_from_html(self, raw_html):
        # print(re.findall("https?://(?:[-\w.])+", raw_html))
        return re.findall("https?://(?:[-\w.])+", raw_html)


if __name__ == "__main__":
    test_wc = WebCrawler()
    test_wc.crawl("https://www.ros.org")

    # Test individual functions
    # raw_html = test_wc.read_raw_html("https://ros.org/")
    # parse_html = test_wc.get_links_from_html(raw_html)
    # print(len(parse_html))
