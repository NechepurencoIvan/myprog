from tkinter import *
from trysql import *

def d_i_t():

    def fbi():
        spsk = reader.get()
        find_for_ill(spsk)
        button_clicked()

    def button_clicked():
        msk = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13]
        atributes = ["#Больного", "Фамилия", "Имя", "Отчество", "Индекс данных", "#донора", "Группа крови", "Резус-фактор",
                     "Дата рож"
                     "дения", "Пол", "Место работы", "Кол-во сдач", "Последняя сдача"]
        arr = find_for_ill(reader.get())
        print(arr)
        j = len(arr)
        print(str(j))
        msk = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        atributes = ["#Больного", "Фамилия", "Имя", "Отчество", "Индекс данных", "Группа крови", "Резус-фактор",
            "Заболевание", "Требуемый объем","#Больного", "Фамилия", "Имя", "Отчество", "Индекс данных", "Группа крови", "Резус-фактор",
            "Заболевание", "Требуемый объем"]
        for i in range(14):
            spsk = []
            for j in range(min(10,len(arr))):
               spsk.append(str(arr[j][msk[i]]))
            string = atributes[i] + "\n" + "\n".join(spsk)
            print(string)
            a[i].configure(text=string)

    a = recount()
    numill = a[0]
    numdon = a[1]
    numpers = a[2]

    root = Tk()
    root["bg"] = "green"
    root.state("zoomed")
    root.title("Река жизни - доноры по больному")

    informator = Label(root)
    informator.configure(text="Введите ФИО болного.Пример: Иванов Иван Иванович", font = "Arial 20")
    informator.place(height = 50, width = 1380 ,x = 0,y = 0)

    reader = Entry(root)
    reader.configure(font = "Arial 20")
    reader.place(height = 50, width = 1220 ,x = 0,y = 50)

    button_search = Button(root)
    button_search.configure(text="Искать", command=fbi)
    button_search.place(height = 50, width = 160 ,x = 1220,y = 50)



    #rf = 0
    #button_rf = Button(root)
    #button_rf.configure(text=("Резус-фактор: " + str(find_rf)), command=ch_rf)
    #button_rf.place(height = 40, width = 160 , x = 1220, y = 200)

    a = []
    labelinfo  = Label(root)
    for i in range(14):
        a.append(Label(root))
        a[i].pack(side = 'left')

    #listbox_blgr=Listbox(root,height=4,width=160,selectmode=EXTENDED)
    #list_blgr=[1,2,3,4]
    #for i in list_blgr:
    #    listbox_blgr.insert(END,i)
    #listbox_blgr.place(x = 1220, y = 240)

    #button_next = Button(root)
    #button_next.configure(text="Следующие", command=next)
    #button_next.place(height = 40, width = 160 , x = 1220, y = 140)

    #button_prev = Button(root)
    #button_prev.configure(text="Предыдущие", command=prev)
    #button_prev.place(height = 40, width = 160 , x = 1220, y = 100)

    root.mainloop()

