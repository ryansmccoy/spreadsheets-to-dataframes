from bs4 import BeautifulSoup
import configparser
import time
from create_names import create_file
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)
import urllib.parse
import lxml
import lxml.html
from lxml.html import parse, tostring, open_in_browser, fromstring


def get_toc_links(filename, w_page_source, URL_WEBSITE,toc_xpath=None):
    create_file(filename, w_page_source, URL_WEBSITE)
    html = lxml.html.fromstring(w_page_source)
    html.make_links_absolute(URL_WEBSITE)
    ab = lxml.html.tostring(html,pretty_print=True, method="html")
    soup = BeautifulSoup(ab, 'lxml')
    links = []
    for link in soup.find_all('a'):
        if 'href' in link.attrs:
            links.append(str(link.attrs['href']))
    urls = []
    for i in links:
        url, fragment = urllib.parse.urldefrag(i)
        urls.append(url)
    urls = f7(urls)
    newurls = []
    for i in urls:
        if 'htm' in i:
            newurls.append(i)
    return(newurls)

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
