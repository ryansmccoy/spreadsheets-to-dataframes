

# try importing scandir and if found, use it as it's a few magnitudes of an order faster than stock os.walk

import sys
import os
# Generate type library so that we can access constants

import process_html_remove_junk
def convertHTML2PDF(htmlPath, pdfPath):
    import win32com.client.makepy
    import win32com.client
    from win32com.client import Dispatch
    from win32com.client.dynamic import ERRORS_BAD_CONTEXT
    import winerror
    win32com.client.makepy.GenerateFromTypeLibSpec('Acrobat')
    # Use Unicode characters instead of their ascii psuedo-replacements
    UNICODE_SNOB = 0
    'Convert an HTML document to PDF format'
    # Connect to Adobe Acrobat
    import win32com.client
    avDoc = win32com.client.DispatchEx('AcroExch.AVDoc')
    avDoc.Open(os.path.abspath(htmlPath), 'html2pdf')
    # Save in PDF format
    pdDoc = avDoc.GetPDDoc()
    pdDoc.Save(win32com.client.constants.PDSaveFull, os.path.abspath(pdfPath))
    pdDoc.Close()
    # Close HTML document without prompting to save
    avDoc.Close(True)

def file_conversion(folder):
    nfolder = os.path.join(folder,'clean')
    #folder = os.path.normpath(sys.argv[1])
    if nfolder is None:
        directory = 'C:\\HTML'
        files = process_html_remove_junk.walk_dir_fullfilename(directory)
    else:
        files=[]
        files = [os.path.join(nfolder, x) for x in os.listdir(nfolder)]
    for filename in files:
        basename = os.path.basename(filename)
        extname = os.path.splitext(basename)
        dirname = os.path.dirname(filename)
        pdf = os.path.join(folder,'pdf', extname[0]+'.pdf')
        try:
            print(pdf)
            convertHTML2PDF(filename, pdf)
        except:
            print('problem with: ' + filename)


