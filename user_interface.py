from tkinter import *
from tkinter import filedialog
from init_vbscript import Convertation


def clicked_from():
    # что произойдет при нажатии Выбрать...  (поле "Откуда достать документы")
    # выбор директории с файлами doc
    dir_from = filedialog.askdirectory()
    path_from.configure(text=dir_from)
    return dir_from


def clicked_to():
    # что произойдет при нажатии Выбрать...  (поле "Куда положить pdf")
    # выбор директории, в которую положить готовые pdf
    dir_to = filedialog.askdirectory()
    path_to.configure(text=dir_to)
    return dir_to


# создаем окно программы 
window = Tk()
window.title("Конвертер doc в pdf")
window.geometry('700x250')

# выбор директории с файлами doc
lbl_from = Label(window, text="Откуда достать документы", font=("Arial Bold", 10))  
lbl_from.grid(column=0, row=0)  
#txt = Entry(window, width=50, text="путь здесь")  
#txt.grid(column=0, row=1)  
path_from = Label(window, text="---выбранный путь здесь---")
path_from.grid(column=0, row=1)
btn_from = Button(window, text="Выбрать...", command=clicked_from)  
btn_from.grid(column=1, row=1)

# выбор директории, в которую положить готовые pdf
lbl_to = Label(window, text="Куда положить pdf", font=("Arial Bold", 10))  
lbl_to.grid(column=0, row=3)  
path_to = Label(window, text="---выбранный путь здесь---", padx=40)   
path_to.grid(column=0, row=4)  
btn_to = Button(window, text="Выбрать...", command=clicked_to)  
btn_to.grid(column=1, row=4)


conv = Convertation(clicked_from(), clicked_to())       # объявляем оъект класса Convertation


def cliced_convert():
    conv.convert()


# кнопка конвертировать
btn_convert = Button(window, text="Опля!", command=cliced_convert)
btn_convert.grid(column=0, row=5)

window.mainloop()