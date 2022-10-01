import re

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
def SendAttribute(path_xml):
    line_id = str()
    line_num = str()
    try:
        with open(path_xml, 'r', encoding='Windows-1251') as files:
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
    # global
    num_out = 1412
    return str(ID[14:-41]) + "-" + str(num_out), str(RCC[24:-38]) + "-" + str(num_out)


def modify_name_xml(path_xml):
    # global
    num_out = 1412
    return str(path_xml.split("//")[-1].split(".")[0]) + str(num_out)


def RedirectFile(path_xml, path_to_main_folder_checks):
    os.chdir(path_to_main_folder_checks)
    for i in os.listdir(os.getcwd()):
        os.chdir(i)
        try:
            sh.copy(path_xml, os.getcwd())
            print("Copy ok")
        except OSError:
            print("Error in copy")
        os.chdir(path_to_main_folder_checks)


def ModifyXMLFile(path_to_main_folder_checks, Id_name, Id_name_modify):
    os.chdir(path_to_main_folder_checks)
    for i in os.listdir(os.getcwd()):
        os.chdir(i)
        for j in os.listdir(os.getcwd()):
            path_local_check_xml_file = os.getcwd() + '//' + j
            print(j)
            try:
                with open(path_local_check_xml_file, 'r', encoding='Windows-1251') as f:
                    xml_data = f.read()
                    xml_data = re.sub(Id_name[14:-41], Id_name_modify, xml_data)
                f.close()
                with open(j, 'w', encoding='Windows-1251') as f:
                    f.write(xml_data)
                f.close()
            except IOError:
                print("Error in modify_in_xml")

        os.chdir(path_to_main_folder_checks)


def ModifyAttributeXMLFile(path_xml, modify_):
    try:
        with open(path, 'r', encoding='Windows-1251') as f:
            xml_file = f.read()
            xml_file = re.sub(Id_file[14:-41], x, xml_file)
            print("Modify file successful")
        f.close()
    except IOError:
        print("Error in ")
    with open(path, 'w', encoding='Windows-1251') as f:
        f.write(xml_file)
    f.close()


# C:\Users\zamot\OneDrive\Документы\GitHub\UPDautoCreate\XMLandXML\ON_NSCHFDOPPRPROS_2BM-2310031475-2012070307370849459200000000000_2BM-9718070427-771801001-20220921-.xml
if __name__ == '__main__':
    # получаем путь
    path = PathXmlInput()

    # исходники
    Id_file, Num_chf = SendAttribute(path)

    # модифиц имя
    name_xml = modify_name_xml(path)

    # for i in os.listdir(getPathChecks()):
    # sh.copy(path, r'C://Users//zamot//OneDrive//Документы\GitHub\UPDautoCreate\Checks\CHCK_01_00')

    # модиф атрибуты
    id_name, rcc_name = modifyIDRCC(Id_file, Num_chf)[0], modifyIDRCC(Id_file, Num_chf)[1]

    # print(x,'\f ', y)

    # with open(path, 'r', encoding='Windows-1251') as files:
    #     xml_data = files.read()
    #     xml_data = re.sub(Id_file[14:-41], x, xml_data)
    #     print(xml_data)
    # files.close()
    #
    # with open(path, 'w', encoding='Windows-1251') as files:
    #     files.write(xml_data)
    # files.close()

    # asdasd =
    getPathChecks = getPathChecks()
    #print(path)
    RedirectFile(path, getPathChecks)

    ModifyXMLFile(getPathChecks, Id_file, id_name)
