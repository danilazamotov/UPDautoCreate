from CreateFoldersToCheck import getPathChecks, AutoParsePathXLSX
import os
import shutil as sh


# Only inputting and checking xml_path for format xml
def PathXmlInput():
    try:
        path_to_xml = r"C:\Users\zamot\OneDrive\Документы\GitHub\UPDautoCreate\XMLandXML\ON_NSCHFDOPPRPROS_2BM-2310031475-2012070307370849459200000000000_2BM-9718070427-771801001-20220921-.xml"
        # str(input("Path to .xml:"))
        if ".xml" in path_to_xml:
            print("Path to .xml is correct")
        else:
            print("Path to .xml is not correct")
    except IOError:
        print("Error in PathXmlInput()")
    return AutoParsePathXLSX(path_to_xml)


# open .xml and send attributes
def SendAttribute(path):
    line_id = str()
    line_num = str()
    try:
        with open(path, 'r', encoding='Windows-1251') as files:
            for line in files:
                try:
                    if "Файл ИдФайл=" in line:
                        line_id = line
                    if "НомерСчФ=" in line:
                        line_num = line
                except AttributeError:
                    print("xml document does not contain attribute/s")
    except IOError:
        print("Failed to open file")

        files.close()
    return line_id, line_num


def modifyIDRCC(ID, RCC):
    #global
    num_out = 1412
    return str(ID[14:-41]) + "_" + str(num_out), str(RCC[24:-38]) + "-" + str(num_out)


def modify_name_xml(path_xml):
    #global
    num_out = 1412
    return str(path_xml.split("//")[-1].split(".")[0]) + str(num_out)

# def asdasd(path_xml, path_new_xml):

# def asd(Id_modify, RCC_modify, Name_modify, ):
    # копируем xml перемещаем в лок папку, там его меняем и идем дальше копировать в другую папку



    # try:
    #     with open(path, 'r', encoding='Windows-1251') as files:
    #         for line in files:
    #             if "Файл ИдФайл=" in line:
    #                 line.replace(line[14:-41], Id_modify)
    #
    #             if "НомерСчФ=" in line:
    #                 line_num = file
    #
    #
    #
    # except IOError:
    #     print("Failed to open file")
    #
       # files.close()

def RangeNameCheck():
    array = 14
    start_int = 1000  # int(input("введите начальный диапазон, с которой начнется проверка в int: "))
    end_int = start_int + (array)  # len()
    x = range(start_int, end_int)
    return x


# C:\Users\zamot\OneDrive\Документы\GitHub\UPDautoCreate\XMLandXML\ON_NSCHFDOPPRPROS_2BM-2310031475-2012070307370849459200000000000_2BM-9718070427-771801001-20220921-.xml
if __name__ == '__main__':
    path = PathXmlInput()
    #Id_file, Num_chf = SendAttribute(path)

    #print(modifyIDRCC(Id_file, Num_chf))

    #print(modify_name_xml(path))

    #for i in os.listdir(getPathChecks()):

    sh.copyfile(path, 'C://Users//zamot//OneDrive//Документы//GitHub//UPDautoCreate\FilePy')