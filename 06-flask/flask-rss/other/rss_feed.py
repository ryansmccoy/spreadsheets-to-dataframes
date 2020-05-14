
# python standard library
import os
import zipfile

import feedparser
# 3rd-party, pip installed libraries
import pandas as pd

pd.set_option("display.float_format", lambda x: "%.5f" % x)  # pandas
pd.set_option("display.max_columns", 100)
pd.set_option("display.max_rows", 100)
pd.set_option("display.width", 600)

pd.set_option('expand_frame_repr', True)
pd.set_option('max_rows', 50)
pd.set_option('display.max_rows', 50)

rss_url = r'http://www.globenewswire.com/AtomFeed/orgclass/1/feedTitle/GlobeNewswire%20-%20News%20about%20Public%20Companiesc'
earnings_url = r'http://www.globenewswire.com/AtomFeed/subjectcode/13-Earnings%20Releases%20And%20Operating%20Results/feedTitle/GlobeNewswire%20-%20Earnings%20Releases%20And%20Operating%20Results'
div_rss = r'http://www.globenewswire.com/AtomFeed/subjectcode/12-Dividend%20Reports%20And%20Estimates/feedTitle/GlobeNewswire%20-%20Dividend%20Reports%20And%20Estimates'
mna_Rss = r'http://www.globenewswire.com/AtomFeed/subjectcode/27-Mergers%20And%20Acquisitions/feedTitle/GlobeNewswire%20-%20Mergers%20And%20Acquisitions'
prnewswire_rss = r'https://www.prnewswire.com/rss/all-news-releases-from-PR-newswire-news.rss'
rss_feeds = r'D:\PROJECTS\presentations\rss_feeds.csv'
pr_rss1 = r'https://www.prnewswire.com/rss/financial-services-latest-news.rss'
nas_rss = r'http://ir.nasdaq.com/rss/news-releases.xml?items=15'
prweb_rss = r'http://www.prweb.com/rss2/daily.xml'

def flatten_json(dictionary):
    """Flatten a nested json file"""
    from itertools import chain, starmap

    def unpack(parent_key, parent_value):
        """Unpack one level of nesting in json file"""
        # Unpack one level only!!!

        if isinstance(parent_value, dict):
            for key, value in parent_value.items():
                temp1 = parent_key + '_' + key
                yield temp1, value
        elif isinstance(parent_value, list):
            i = 0
            for value in parent_value:
                temp2 = parent_key + '_' + str(i)
                i += 1
                yield temp2, value
        else:
            yield parent_key, parent_value
            # Keep iterating until the termination condition is satisfied

    while True:
        # Keep unpacking the json file until all values are atomic elements (not dictionary or list)
        dictionary = dict(chain.from_iterable(starmap(unpack, dictionary.items())))
        # Terminate condition: not any value in the json file is dictionary or list
        if not any(isinstance(value, dict) for value in dictionary.values()) and \
                not any(isinstance(value, list) for value in dictionary.values()):
            break

    return dictionary

from datetime import datetime
df = pd.read_csv(rss_feeds)

data_dir = os.path.join(os.getcwd(), "data\\rss")

import pandas as pd

keep = ('title', 'link', 'published', 'published_parsed', 'summary', 'id')

df_filtered = df[df['CATEGORY'].isin(['business', 'politics', 'science', 'tech','general'])]
df_filtered_us = df_filtered[df_filtered['COUNTRY_CODE'].isin(['US'])]

_entries = []
all_entries = []

from urllib import parse
import tldextract

for i, feed in df_filtered_us.iterrows():
    print(feed)
    url = "https://" + feed.URL
    parsed_url = parse.urlparse(url)
    print(parsed_url)
    dom = tldextract.extract(url)
    # filename = f'{dom.domain}.csv'
    folderpath = os.path.join(f'.\\data\\rss\\{dom.domain}')

    if not os.path.exists(folderpath):
        os.mkdir(folderpath)

    filename =  f"{datetime.now().strftime('%Y-%m-%dT%H-%M-%S')}.csv"

    filepath = os.path.join(folderpath, filename)

    print(filepath)

    _entries = []

    _feed = feedparser.parse(url)

    if len(_feed.entries) == 0:
        print("FOUND 0 Entries\n\n")
        url = "http://" + feed.URL
        _feed = feedparser.parse(url)

    for entry in _feed.entries:

        final_dict = flatten_json(entry)
        _entries.append(final_dict)

        _title = entry.get("title", "No Title")
        _published = entry.get('updated', None)

        if not _published:
            _published = entry.get('published', None)

        headline_dict = {"title": _title, "published": _published, "source": dom.domain }

        all_entries.append(headline_dict)

    df_entries = pd.DataFrame(_entries)

    df_entries['datasource'] = dom.domain
    df_entries.to_csv(filepath)

df = pd.DataFrame(all_entries)
df = df.sort_values('published', ascending=False)
df.reset_index(inplace=True,drop=True)
df.to_csv(os.path.join(f"headlines_{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.csv"))
