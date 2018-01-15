import urllib.request
import requests
import json
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import sys


def search(url, visited, current, target):
    if current >= target:
        return
    current_num = current + 1
    target_num = target

    url_parse = urlparse(url)
    url_scheme = url_parse.scheme
    url_hostname = url_parse.hostname
    url_path = url_parse.path

    my_page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(my_page, 'lxml')
    html_get = str(soup.prettify())

    requests.post("http://localhost:8000/page/", json.dumps({"Title": url_path, "Body": html_get}))

    for line in soup.find_all('a', href=True):

        if '//' not in line['href'] and '#' != str(line['href'])[0] \
                and line['href'] not in visited \
                and ":" not in line['href'] and "=edit" not in line['href']:

            visited.append(line['href'])
            new_url = url_scheme + "://" + url_hostname + line['href']

            search(new_url, visited, current_num, target_num)

if __name__ == '__main__':
    if len(sys.argv) > 0:
        search(sys.argv[1], [], 0, int(sys.argv[2]))
    else:
        print("not valid")
