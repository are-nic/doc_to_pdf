import os

folder_from = os.getcwd() + r'\words'   # папка, где лежит тонна word файлов
folder_to = os.getcwd() + r'\txts'      # папка, куда будем сохранять 


def convert(file_name):
    str1 = folder_from + r"/" + file_name
    str2 = folder_to + r"/" + file_name[:file_name.rfind('.')] 
    os.system('converter.vbs  "' + str1 + '" "' + str2 + '"')   # запуск скрипта