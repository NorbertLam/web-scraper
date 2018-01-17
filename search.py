import urllib.request
import requests
import json
import sys
import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def search(url, visited, current, target):
    if current >= target:
        return
    current_num = current + 1
    target_num = target

    endpoint = os.environ.get('ENDPOINT')
    url_parse = urlparse(url)
    url_scheme = url_parse.scheme
    url_hostname = url_parse.hostname
    url_path = url_parse.path

    scrapedPage = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(scrapedPage, 'lxml')
    html_get = str(soup.prettify())

    requests.post(endpoint, json.dumps({"url": url_path, "html": html_get}))

    for line in soup.find_all('a', href=True):
        if '//' not in line['href'] and '#' != str(line['href'])[0] \
                and line['href'] not in visited \
                and ":" not in line['href'] and "=edit" not in line['href']:

            visited.append(line['href'])
            new_url = url_scheme + "://" + url_hostname + line['href']

            search(new_url, visited, current_num, target_num)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        search(sys.argv[1], [], 0, int(sys.argv[2]))
    else:
        print("usage: search.py url depth")
