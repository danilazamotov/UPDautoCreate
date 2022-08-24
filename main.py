from ast import parse
from dataclasses import replace
from importlib.resources import path
import os
import sys
from turtle import shape
from unittest.mock import patch
import numpy as np
import pandas as pd

def ConnectXLSX(path):
    local_path = path
    try:
        local_path1 = pd.read_excel(local_path, sheet_name= None, header=None, index_col=None, converters=None)
        #print("имена проверок: ", local_path1)

    except OSError:
        print ("Could not open/read file:", local_path)
        sys.exit
    return local_path1

def AutoParsePathXLSX(path):
    local_path = path.replace ('\\', '//')
    return local_path

def ConnectToFolderToCreate(path, name):
    #os.chdir(path)
    name_path = path + "\\" +  name
    #print(name_path)
    try:
        os.mkdir(name)
    except:
        #print('Папка с таким именем уже создана')
        pass
    return name_path

    #ArrayToCheck - необработанный массив с именами проверок
def CreateFoldersForChecks(ArrayToCheck, path_main_folder):
    os.chdir(path_main_folder)
    # нужно будет получить sheet_name xlsx
    local_array = np.array(ArrayToCheck['Лист1'].values.tolist()).flatten()

    
    for i in local_array:
        try:
            os.makedirs(i)
        except:
            pass
            #print("Папки с проверками уже созданы")


main_folder = 'Test'
path_to_FC = 'C:\Projects\Python'
path = 'C://Users\zamot\Desktop\Новая таблица.xlsx'


if __name__ == '__main__':
    array_xlsx = pd.array([])

    #print("Введите полный путь для xlsx файла, который содержит названия проверок")
    #path_xlsx = input()
    x = (AutoParsePathXLSX(path))
    #print("осуществляется чтение файла")
    
    #Получаем корректный путь
    array_xlsx = ConnectXLSX(AutoParsePathXLSX(x))    
    
    #Получаем путь к корневому каталогу
    path_main_folder  = ConnectToFolderToCreate(path_to_FC, main_folder)
    
    #Создаем папки с проверками в корневой папке
    CreateFoldersForChecks(array_xlsx, path_main_folder)