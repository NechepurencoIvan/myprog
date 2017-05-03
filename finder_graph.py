from tkinter import *
from trysql import *

find_rf = 0
def finder_donors():
    offs = 0
    def next():
        # global offs
        # offs += 1
        print(offs)

    def button_clicked():
        msk = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13]
        atributes = ["#", "Фамилия", "Имя", "Отчество", "Индекс данных", "#донора", "Группа крови", "Резус-фактор",
                     "Дата рож"
                     "дения", "Пол", "Место работы", "Кол-во сдач", "Последняя сдача"]
        for i in range(13):
            a[i].configure(
                text=atributes[i] + "\n" + find_donors(int(listbox_blgr.curselection()[0]) + 1, find_rf, 0, msk[i]))

    def ch_rf():
        global find_rf
        if (find_rf == 0):
            find_rf = 1
        else:
            find_rf = 0
        button_rf.configure(text=("Резус-фактор" + str(find_rf)))

    root = Tk()
    root["bg"] = "green"
    root.state("zoomed")
    root.title("Река жизни - поиск доноров")


    button = Button(root)
    button.configure(text="Поиск", command=button_clicked)
    button.place(height = 40, width = 160 , x = 1220, y = 600)

    rf = 0
    button_rf = Button(root)
    button_rf.configure(text=("Резус-фактор: " + str(find_rf)), command=ch_rf)
    button_rf.place(height = 40, width = 160 , x = 1220, y = 400)

    a = []
    #labelinfo  = Label(root)
    for i in range(13):
        a.append(Label(root))
        a[i].pack(side = 'left')

    listbox_blgr=Listbox(root,height=4,width=160,selectmode=EXTENDED)
    list_blgr=[1,2,3,4]
    for i in list_blgr:
        listbox_blgr.insert(END,i)
    listbox_blgr.place(x = 1220, y = 440)

    #button_next = Button(root)
    #button_next.configure(text="Следующие", command=next())
    #button_next.place(height = 40, width = 160 , x = 1220, y = 100)

    root.mainloop()

