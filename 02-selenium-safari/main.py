

import os
import selenium
from selenium import webdriver
import create_names
from create_names import create_folder_path_from_url, create_filename_from_url, create_file
from zip_folder import zip_directory
from merge_pdf_files import pyMerger
import time
import gather_links_for_processing
from gather_links_for_processing import get_toc_links
import random
import process_html_remove_junk
import html_to_pdf


def file_merge(directory):
    for path, dirnames, files in os.walk(directory):
        pyMerger(path)
        print(path)

def post_process():
    file_merge(BASE_DIR)
    zip_directory(BASE_DIR)

def pause_for_random_time():
    time.sleep(random.randint(3,7))

def process_html_files(directory=None):
    files_processed = process_html_remove_junk.process_html_files_removing_junk(directory)
    return files_processed

def process_cleaned_files_into_pdf(directory):
    files_processed_pdf = html_to_pdf.file_conversion(directory)
    return files_processed_pdf

def grab_urls_from_file(INPUT_FILE):
    file = INPUT_FILE
    urls = []
    list_of_list_of_filenames=[]
    with open(file, 'r') as f:
        urls = f.read().splitlines()
    if len(urls) < 1:
        urls = [sys.argv[1]]
        print(urls)
    return urls

def main():
    '''
    function which calls file with urls to process
    '''
    if len(sys.argv) < 2:
            sys.exit(0)

    w = webdriver.Chrome()

    domain_url, base_login = URL_WEBSITE, URL_LOGIN
    w.get(domain_url + base_login)
    loginElem = w.find_element_by_name('email')
    loginElem.send_keys(USERNAME)
    loginPass = w.find_element_by_name('password1')
    loginPass.send_keys(PASSWORD)
    time.sleep(3)
    loginPass.submit()
    time.sleep(3)

    urls = grab_urls_from_file(INPUT_FILE)

    for url in urls:
        w.get(url)
        base_dir = os.path.abspath(os.sep)
        path = create_names.create_folder_path_from_url(BASE_DIR, url)
        filename = os.path.join(path,create_names.create_filename_from_url(url) + '(t).html')
        page_source = w.page_source
        toc_table_only = page_source
        toc = gather_links_for_processing.get_toc_links(filename, w.page_source, URL_WEBSITE)
        for webpage_url in toc:
            try:
                w.get(webpage_url)
                filename = create_names.create_filename_from_url(w.current_url)
                fout = create_names.create_file(os.path.join(path,filename + '.html'), w.page_source, URL_WEBSITE)
            except:
                print('something broke: ', filename)
            pause_for_random_time()
        list_of_list_of_filenames = process_html_files(path)
        process_cleaned_files_into_pdf(path)
        #pyMerger(directory)









if __name__ == '__main__':
    main()
