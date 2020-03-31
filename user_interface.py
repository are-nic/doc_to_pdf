from tkinter import *


def clicked_from():
    # что произойдет при нажатии Выбрать...  
    lbl_from.configure(text="Путь был выбран")


def clicked_to():
    lbl_to.configure(text="Путь был выбран") 


# создаем окно программы 
window = Tk()
window.title("Конвертер doc в pdf")
window.geometry('500x250')

# выбор директории с файлами doc
lbl_from = Label(window, text="Откуда достать документы")  
lbl_from.grid(column=0, row=0)  
txt = Entry(window,width=50)  
txt.grid(column=0, row=1)  
btn_from = Button(window, text="Выбрать...", command=clicked_from)  
btn_from.grid(column=1, row=1)

# выбор директории, в которую положить готовые pdf
lbl_to = Label(window, text="Куда положить pdf")  
lbl_to.grid(column=0, row=3)  
txt = Entry(window,width=50)  
txt.grid(column=0, row=4)  
btn_to = Button(window, text="Выбрать...", command=clicked_to)  
btn_to.grid(column=1, row=4)
window.mainloop()