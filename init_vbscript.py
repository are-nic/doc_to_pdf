import os

folder_from = os.getcwd() + r'\Desktop\Python books\docs'   # папка, где лежит тонна word файлов
folder_to = os.getcwd() + r'\Desktop\ежегодная проверка знаний'   # папка, куда будем сохранять 


def convert(file_name):
    path_to_vbs = r'C:\Users\Руслан\Documents\doc_to_pdf\\'        
    path_to_docs = folder_from + r"/" + file_name
    path_for_pdf = folder_to + r"/" + file_name[:file_name.rfind('.')] 
    os.system('CScript {}converter.vbs "{}" "{}"'.format(path_to_vbs, path_to_docs, path_for_pdf))   # запуск скрипта в cmd


for subdir, dirs, files in os.walk(folder_from):
    for file in files:
        convert(file)