import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import global_file
import re


def search(url):
    if global_file.counter >= 4:
        return
    global_file.counter += 1

    my_url = url
    url_parse = urlparse(my_url)
    url_scheme = url_parse.scheme
    url_front = url_parse.hostname
    url_end = url_parse.path
    re_name = re.sub(r'\W+', '', url_end)

    my_page = urllib.request.urlopen(my_url).read()
    soup = BeautifulSoup(my_page, 'lxml')
    html_get = str(soup.prettify())

    file = open("archive/" + re_name + ".html", "w", encoding='utf-8')
    file.write(html_get)
    file.close()

    for line in soup.find_all('a', href=True):

        if '//' not in line['href'] and '#' != str(line['href'])[0] \
                and line['href'] not in global_file.visited \
                and ":" not in line['href']:

            global_file.visited.append(line['href'])
            new_url = url_scheme + "://" + url_front + line['href']

            search(new_url)
