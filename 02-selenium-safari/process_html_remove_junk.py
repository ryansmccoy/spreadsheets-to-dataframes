
import os
from bs4 import BeautifulSoup
import create_names
from create_names import create_filenames_for_conversion



def grab_junk_tag(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
    bsObj = BeautifulSoup(data, "html.parser")
    head_elements_blacklist = ['topbar t-topbar']
    body_elements_blacklist = ['expanded', 'annotator-modal-wrapper annotator-editor-modal annotator-editor annotator-hide', 'annotator-modal-wrapper annotator-delete-confirm-modal', 'annotator-adder','sbo-reading-menu sbo-menu-top', 'interface-controls interface-controls-top', 'sample-message', 'font-flyout','t-sbo-next sbo-next sbo-nav-bottom', 't-sbo-next sbo-next sbo-nav-top', 't-sbo-prev sbo-prev sbo-nav-bottom', 't-sbo-prev sbo-prev sbo-nav-top', 'reading-controls-bottom']
    footer_elements_blacklist = ['pagefoot t-pagefoot']
    html_elements_blacklists = [{'header': head_elements_blacklist}, {'div': body_elements_blacklist}, {'footer': footer_elements_blacklist}]

    for elements in html_elements_blacklists:
        for element, tags in elements.items():
            for tag in tags:
                try:
                    temp = bsObj.find(element, {'class': tag})
                    temp.decompose()
                    #print('processed: ' + element + ' ' + tag)
                except:
                    print('error: ' + tag)
                    continue
    return(bsObj)

def check_for_folder_and_create(destfolder,additional=None):
    if additional != None:
        new_folders = []
        for folder in additional:
            newfolder = os.path.join(destfolder,folder)
            if not os.path.isdir(newfolder):
                os.makedirs(newfolder)
            new_folders.append(newfolder)
        return new_folders
    if not os.path.isdir(destfolder):
        os.makedirs(destfolder)
        return destfolder
    

def get_fullfilepaths_files_in_folder(folder_to_process, extfilter=None):
    files_in_folder = [os.path.join(folder_to_process, x) for x in os.listdir(folder_to_process) if extfilter in x]
    return files_in_folder

def walk_dir_fullfilename(directory, extfilter=None):
    all_files = []
    for path, dirnames, files in os.walk(directory):
        for file in files:
            filepath, filename = path, file
            fullfilepath = os.path.join(path, file)
            if extfilter != None:
                if extfilter in fullfilepath and '(clean)' not in fullfilepath:
                    all_files.append(fullfilepath)
                else:
                    pass
            else:
                all_files.append(fullfilepath)
    return all_files

#walk_test=walk_dir_fullfilename(directory, extfilter='htm')

def process_html_files_removing_junk(directory):
    #folder = os.path.normpath(sys.argv[1])
    if directory is None:
        directory = 'C:\\HTML'
        files = walk_dir_fullfilename(directory)
    else:
        files = get_fullfilepaths_files_in_folder(directory, extfilter='htm')
    for filename in files:
        try:
            list_of_list_of_filenames = []
            basename = os.path.basename(filename)
            extname = os.path.splitext(basename)
            dirname = os.path.dirname(filename)
            destfolder = directory
            filename_html, filename_pdf = create_names.create_filenames_for_conversion(destfolder, filename, extname[1])
            filepath = check_for_folder_and_create(destfolder,additional=["clean","pdf","html"])
            pdf = os.path.join(filepath[1],filename_pdf)
            html_clean = os.path.join(filepath[0], filename_html)
            try:
                bsObj = grab_junk_tag(filename)
            except:
                print('error' + html)
            try:
                with open(html_clean, "w", encoding='utf-8') as file:
                    file.write(str(bsObj.decode_contents))
            except:
                with open(html_clean, "w", encoding='utf-8') as file:
                    file.write(str(bsObj.decode_contents))
            list_of_list_of_filenames.append([filename, html_clean, pdf])
        except:
            print('problem with:' + filename)
    return list_of_list_of_filenames