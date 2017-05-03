from tkinter import *
from trysql import *

def adding_person(f):
    def button_clicked():
        s = reader.get()
        print(s)
        if (len(s) > 0):
            addpers(reader.get())
            reader.delete(0, 'end')
            debug_table("SELECT * FROM persons")
            root.destroy()
            if f == 1:
                adding_donor()


    root = Tk()
    root["bg"] = "green"
    root.state("zoomed")
    root.title("Река жизни - добавление донора")

    informator = Label(root)
    informator.configure(text="Введите ФИО, контактные даннные\nПример: Иванов Иван Иванович 123456789", font = "Arial 20")
    informator.pack(side = "top", fill = "x")

    reader = Entry(root)
    reader.configure(font = "Arial 20")
    reader.pack(side = "top", fill = "x")

    button = Button(root)
    button.configure(text="Добавить", command=button_clicked)
    button.pack(side = "top", fill = "x")


    root.mainloop()

def adding_donor():
    def button_clicked():
        s = reader.get()
        print(s)
        if (len(s) > 0):
            ADDDONOR(reader.get())
            reader.delete(0, 'end')
            debug_table("SELECT * FROM donors")
            root_ad.destroy()
    root_ad = Tk()
    root_ad["bg"] = "green"
    root_ad.state("zoomed")
    root_ad.title("Река жизни - добавление донора")

    informator = Label(root_ad)
    informator.configure(text="Введите группу крови, резус-фактор, дату рождения, пол, место работы, колличество сдач "
"крови, дату последней сдачи\nПример: 1 1 1998-01-20 woman RNPC 32 2012-01-05", font = "Arial 20")
    informator.pack(side = "top", fill = "x")

    reader = Entry(root_ad)
    reader.configure(font = "Arial 20")
    reader.pack(side = "top", fill = "x")

    button = Button(root_ad)
    button.configure(text="Добавить", command=button_clicked)
    button.pack(side = "top", fill = "x")

    root_ad.mainloop()