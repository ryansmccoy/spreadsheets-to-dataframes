import os
import sys
import time
import urllib.parse
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import configparser


config = configparser.ConfigParser()
config.read(r'C:\Projects\@Scripts\CONFIG\web_html_pdf_zip.cfg')
URL_REPLACE = config['Settings']['URL_REPLACE']
URL_WEBSITE = config['Settings']['URL_WEBSITE']

def create_filenames_for_conversion(filepath, filename, file_extention):
    print(filepath, filename)
    timestr = time.strftime("%Y%m%d-%H%M%S",time.localtime(os.path.getmtime(os.path.join(filepath, filename))))
    filename = filename.replace(file_extention,"")
    filename = filename.translate(dict((ord(char), None) for char in '\/*?:"<>|,.'))
    filename_html, filename_pdf = os.path.join(timestr + '_' + filename + '(clean)' + file_extention), os.path.join(timestr+'_'+filename + '(clean).pdf')
    print('starting creation of: ' + filename_html)
    return filename_html, filename_pdf


def create_filename_from_url(url):
    url, fragment = urllib.parse.urldefrag(url)
    parsed = urllib.parse.urlsplit(url)
    stripped = parsed.path.replace(URL_REPLACE, '')
    filename = stripped.translate(dict((ord(char), None) for char in '\/*?:"<>|'))
    print(filename)
    return filename

def create_folder_path_from_url(base_dir, url):
    path = os.path.join(base_dir, str(url.split("/")[5]+"_"+url.split("/")[6]).translate(dict((ord(char), None) for char in '\/*?:"<>|')))
    if os.path.exists(path) != True:
        os.makedirs(path)
    print(path)
    return path


def create_file(filename, w_page_source, URL_WEBSITE):
    d = pq(w_page_source, parser='html')
    ab = d.make_links_absolute(URL_WEBSITE)
    soup = BeautifulSoup(ab.html(), "html.parser")
    try:
        with open(filename, "w", encoding='utf-8') as f: 
            f.write(str(soup.decode_contents))
    except:
        print('something broke: ', filename)
    return filename


