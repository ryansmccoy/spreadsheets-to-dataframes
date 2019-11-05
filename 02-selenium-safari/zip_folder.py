import os
import zipfile
import shutil

def zip_folder(folder_path, output_path):
    parent_folder = os.path.dirname(folder_path)
    # Retrieve the paths of the folder contents.
    contents = os.walk(folder_path)
    try:
        zip_file = zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED)
        for root, folders, files in contents:
            # Include all subfolders, including empty ones.
            for folder_name in folders:
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(parent_folder + '\\','')
                print("Adding {:d} to archive.".format(absolute_path))
                zip_file.write(absolute_path, relative_path)
            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                relative_path = absolute_path.replace(parent_folder + '\\','')
                print ("Adding '{:s}' to archive.".format(absolute_path))
                zip_file.write(absolute_path, relative_path)
        print("'{:s}' created successfully.".format(output_path))
    except IOError: 
        print (message)
        sys.exit(1)
    except OSError:
        print (message)
        sys.exit(1)
    except zipfile.BadZipfile:
        print (message)
        sys.exit(1)
    finally:
        zip_file.close()
        shutil.rmtree(folder_path) 

def zip_directory(directory):
    folders =  [ name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name)) ]
    for i in folders:
        zip_folder(os.path.join(directory, i), os.path.join(directory, i + ".zip"))

