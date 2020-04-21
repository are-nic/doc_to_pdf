import os

#folder_from = os.getcwd() + r'\Desktop\Python books\docs'   # папка, где лежит тонна word файлов
#folder_to = os.getcwd() + r'\Desktop\ежегодная проверка знаний'   # папка, куда будем сохранять 


class Convertation:
    def __init__(self, folder_from, folder_to):
        self.folder_from = folder_from
        self.folder_to = folder_to


    def convert(self):
        path_to_vbs = os.getcwd() + r'\converter.vbs'
        for subdir, dirs, files in os.walk(self.folder_from):
            for file_name in files:
                path_to_docs = self.folder_from + r"/" + file_name
                path_for_pdf = self.folder_to + r"/" + file_name[:file_name.rfind('.')] 
                # запуск скрипта в cmd
                os.system('CScript {}converter.vbs "{}" "{}"'.format(path_to_vbs, path_to_docs, path_for_pdf))