import os
import sys
import numpy as np
import pandas as pd


x = r'C:\Users\zamot\OneDrive\Документы\GitHub\UPDautoCreate\File\Checks_list.xlsx'



def AutoParsePathXLSX(Parse_path):
    return Parse_path.replace('\\', '////')


# func read-only data from .xlsx and returns an array of test names (str format)
def ConnectXLSX(path_to_XLSX):
    try:
        list_checks = pd.read_excel(AutoParsePathXLSX(path_to_XLSX), sheet_name=None, header=None, index_col=None)
    except OSError:
        print("Could not open/read file:", path_to_XLSX)
        sys.exit()
    return np.array(list_checks['Лист1'].values)


def CreateCatalogForChecks(Path_to_catalog):
    name_folder_to_checks = "Checks"
    os.chdir(Path_to_catalog)
    try:
        path_to_folder_to_checks = os.getcwd() + "\\" + name_folder_to_checks
        os.mkdir(x)
    except OSError:
        print("Folder with name: %s. Already has created on path: %s" % (name_folder_to_checks, os.getcwd()))
    return path_to_folder_to_checks


def CreateFoldersForChecks(array, path):
    try:
        os.chdir(path)
        for name in array.flatten():
            try:
                os.mkdir(path + "\\" + str(name))
                print("Folders with check created:", name)
            except OSError:
                pass
        print("Folders created successfully")
    except IOError:
        print("Error in CreateFoldersForChecks()")
    return path


# Delete Folders, access is denied ;)
# DeleteFolders(_)
def DeleteFolders(list_dir_path_to_folders):
    for folder in os.listdir(list_dir_path_to_folders):
        try:
            os.remove(os.path.join(str(list_dir_path_to_folders), folder))
            print("Folders in %s removed" % list_dir_path_to_folders)
        except OSError:
            print("Error DeleteFolders")


def getPathChecks():
    folders_path = r'C:\Users\zamot\OneDrive\Документы\GitHub\UPDautoCreate'

    return CreateFoldersForChecks(ConnectXLSX(x), CreateCatalogForChecks(folders_path))

