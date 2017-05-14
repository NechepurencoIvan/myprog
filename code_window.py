import sqlite3
from tkinter import *
from trysql import *

def contact_window():
    def button_clicked():
        c = reader.get()
        j = get_cd(c)
        print(j)
        reader.insert(0,str(j))

    root = Tk()
    root["bg"] = "green"
    #root.state("zoomed")
    root.title("Река жизни - получить контакты")

    informator = Label(root)
    informator.configure(text="Введите номер данных", font = "Arial 20")
    informator.pack(side = "top", fill = "x")

    reader = Entry(root)
    reader.configure(font = "Arial 20")
    reader.pack(side = "top", fill = "x")

    button = Button(root)
    button.configure(text="искать", command=button_clicked,font = "Arial 20")
    button.pack(side = "top", fill = "x")