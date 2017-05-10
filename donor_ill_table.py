from tkinter import *
from trysql import *

def d_i_t():


    root = Tk()
    root["bg"] = "green"
    root.state("zoomed")
    root.title("Река жизни - поиск доноров")

    rf = 0
    button_rf = Button(root)
    button_rf.configure(text=("Резус-фактор: " + str(find_rf)), command=ch_rf)
    button_rf.place(height = 40, width = 160 , x = 1220, y = 200)

    a = []
    #labelinfo  = Label(root)
    for i in range(13):
        a.append(Label(root))
        a[i].pack(side = 'left')

    listbox_blgr=Listbox(root,height=4,width=160,selectmode=EXTENDED)
    list_blgr=[1,2,3,4]
    for i in list_blgr:
        listbox_blgr.insert(END,i)
    listbox_blgr.place(x = 1220, y = 240)

    button_next = Button(root)
    button_next.configure(text="Следующие", command=next)
    button_next.place(height = 40, width = 160 , x = 1220, y = 140)

    button_prev = Button(root)
    button_prev.configure(text="Предыдущие", command=prev)
    button_prev.place(height = 40, width = 160 , x = 1220, y = 100)

    reader = Entry(root)
    reader.configure(font = "Arial 20")
    reader.place(height = 50, width = 700 ,x = 100,y = 655)

    informator = Label(root)
    informator.configure(text="Введите ФИО болного.Пример: Иванов Иван Иванович", font = "Arial 20")
    informator.place(height = 50, width = 700 ,x = 100,y = 0)

    button_dnr = Button(root)
    button_dnr.configure(text="Искать", command=fbd)
    button_dnr.place(height = 50, width = 160 ,x = 1220,y = 655)

    root.mainloop()

