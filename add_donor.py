from tkinter import *
from trysql import *

def adding_person(f):
#    a = recount()
#    numill = a[0]
#    numdon = a[1]
#    numpers = a[2]
    def button_clicked():
        s = reader.get()
        if (len(s) > 0):
            root_ap.destroy()
            adding_cd(f,s)

    root_ap = Tk()
    root_ap["bg"] = "green"
    #root.state("zoomed")
    root_ap.title("Река жизни - добавление человека")

    informator = Label(root_ap)
    informator.configure(text="Введите ФИО, контактные даннные\nПример: Иванов Иван Иванович 123456789", font = "Arial 20")
    informator.pack(side = "top", fill = "x")

    reader = Entry(root_ap)
    reader.configure(font = "Arial 20")
    reader.pack(side = "top", fill = "x")

    button = Button(root_ap)
    button.configure(text="Добавить", command=button_clicked,font = "Arial 20")
    button.pack(side = "top", fill = "x")

    root_ap.mainloop()

def adding_cd(f,s1):
    def button_clicked():
        s = reader.get()
        root1.destroy()
        if f == 1:
            adding_donor(s1,s)
        else:
            adding_ill(s1,s)

    root1 = Tk()
    root1["bg"] = "green"
    #root.state("zoomed")
    root1.title("Река жизни - добавление человека")

    informator = Label(root1)
    informator.configure(text="Введите контактные данные", font = "Arial 20")
    informator.pack(side = "top", fill = "x")

    reader = Entry(root1)
    reader.configure(font = "Arial 20")
    reader.pack(side = "top", fill = "x")

    button = Button(root1)
    button.configure(text="Добавить", command=button_clicked,font = "Arial 20")
    button.pack(side = "top", fill = "x")


    root1.mainloop()
    return 1

def adding_donor(s1,s2):
    def button_clicked():
        s = reader.get()
        if (len(s) > 0):
            ADDDONOR(reader.get())
            cd = get_unused_ncd()
            ya_ustal_pridumivat_imena_functiyam(cd, s2)
            addpers(s1,cd)
            reader.delete(0, 'end')
            debug_table("SELECT * FROM donors")
            root_ad.destroy()
    root_ad = Tk()
    root_ad["bg"] = "green"
    #root_ad.state("zoomed")
    root_ad.title("Река жизни - добавление донора")

    informator = Label(root_ad)
    informator.configure(text="Введите группу крови, резус-фактор, дату рождения, пол, место работы,\n колличество"
" сдач крови, дату последней сдачи\nПример: 1 1 1998-01-20 woman RNPC 32 2012-01-05", font = "Arial 20")
    informator.pack(side = "top", fill = "x")

    reader = Entry(root_ad)
    reader.configure(font = "Arial 20")
    reader.pack(side = "top", fill = "x")

    button = Button(root_ad)
    button.configure(text="Добавить", command=button_clicked,font = "Arial 20")
    button.pack(side = "top", fill = "x")

    root_ad.mainloop()

def adding_ill(s1,s2):
    print("cdfd")
    def button_clicked():
        s = reader.get()
        if (len(s) > 0):
            ADDILL(reader.get())
            cd = get_unused_ncd()
            ya_ustal_pridumivat_imena_functiyam(cd, s2)
            addpers(s1,cd)
            reader.delete(0, 'end')
            root_ad.destroy()
    root_ad = Tk()
    root_ad["bg"] = "green"
    #root_ad.state("zoomed")
    root_ad.title("Река жизни - добавление больного")

    informator = Label(root_ad)
    informator.configure(text="Введите группу крови, резус-фактор, заболевание, требуемый объем крови\nПример: 1 1 "
"injuries 4", font = "Arial 20")
    informator.pack(side = "top", fill = "x")

    reader = Entry(root_ad)
    reader.configure(font = "Arial 20")
    reader.pack(side = "top", fill = "x")

    buttondnr = Button(root_ad)
    buttondnr.configure(text="Добавить", command=button_clicked,font = "Arial 20")
    buttondnr.pack(side = "top", fill = "x")


    root_ad.mainloop()