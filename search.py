import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re

def search(url):

    my_url = url
    url_parse = urlparse(my_url)
    url_scheme = url_parse.scheme
    url_front = url_parse.hostname
    url_end = url_parse.path
    file_name = url_front + url_end + ".html"

    my_page = urllib.request.urlopen(my_url).read()
    soup = BeautifulSoup(my_page, 'lxml')
    html_get = soup.prettify()
    #print(html_get)

    for line in soup.find_all('a', href=re.compile("(/wiki/)+([A-Za-z0-9_:()])+")):
        #print(line['href'])
        new_url = url_scheme + "://" + url_front + line['href']
        #print(my_url + " " + new_url)

        file = open(file_name, "w", encoding='utf-8')
        file.write(html_get)
        file.close()

        search(new_url)