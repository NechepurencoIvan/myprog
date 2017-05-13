from tkinter import *
from trysql import *

find_rf = 0
find_acc = 0
find_offs = 0
def finder_donors():
    a = recount()
    numill = a[0]
    numdon = a[1]
    numpers = a[2]
    def next():
        global find_offs
        find_offs += 1
        button_clicked()

    def prev():
        global find_offs
        if find_offs > 0:
            find_offs -= 1
        button_clicked()

    def fbd():
        spsk = reader.get()
        results = find_by_ill(spsk)
        if(not find_rf == results[0][1]):
            ch_rf()
        listbox_blgr.select_set(results[0][0] - 1)
        search_button_clicked()

    #def srch_ill


    def button_clicked():
        msk = [5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13]
        atributes = ["#Больного", "Фамилия", "Имя", "Отчество", "Индекс данных", "#донора", "Группа крови", "Резус-фактор",
                     "Дата рож"
                     "дения", "Пол", "Место работы", "Кол-во сдач", "Последняя сдача"]
        for i in range(13):
            a[i].configure(
                text=atributes[i] + "\n" + find_donors(int(listbox_blgr.curselection()[0]) + 1, find_rf, find_offs, msk[i]))

    def search_button_clicked():
        global find_offs
        find_offs = 0
        button_clicked()

    def ch_rf():
        global find_rf
        if (find_rf == 0):
            find_rf = 1
        else:
            find_rf = 0
        button_rf.configure(text=("Резус-фактор" + str(find_rf)))

    def getagrfrbool(b):
        if b == 0:
            return "Нет"
        return "Да"

    def ch_acc():
        global find_acc
        if (find_acc == 0):
            find_acc = 1
        else:
            find_acc = 0
        button_acc.configure(text=("Согласие: " + getagrfrbool(find_acc)))

    def link():
        string = reader.get()
        a = search_ill_by_name(string.split())
        spsk = [a, reader_dnr_id.get(), find_acc]
        don_ill_link_add(spsk)

    root = Tk()
    root["bg"] = "green"
    root.state("zoomed")
    root.title("Река жизни - поиск доноров")


    button = Button(root)
    button.configure(text="Поиск", command = search_button_clicked)
    button.place(height = 40, width = 160 , x = 1220, y = 400)

    #rf = 0
    button_rf = Button(root)
    button_rf.configure(text=("Резус-фактор: " + str(find_rf)), command=ch_rf)
    button_rf.place(height = 40, width = 160 , x = 1220, y = 200)

    button_acc = Button(root)
    button_acc.configure(text=("Согласие: " + getagrfrbool(find_rf)), command=ch_acc)
    button_acc.place(height = 40, width = 160 , x = 900, y = 600)

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

    reader_dnr_id = Entry(root)
    reader_dnr_id.configure(font = "Arial 20")
    reader_dnr_id.place(height = 50, width = 50 ,x = 800,y = 655)

    button_add_link = Button(root)
    button_add_link.configure(text="Приписать донора", command = link)
    button_add_link.place(height = 50, width = 160 , x = 850, y = 655)

    informator = Label(root)
    informator.configure(text="Введите ФИО болного.Пример: Иванов Иван Иванович", font = "Arial 20")
    informator.place(height = 50, width = 700 ,x = 100,y = 605)

    button_dnr = Button(root)
    button_dnr.configure(text="Искать", command = fbd)
    button_dnr.place(height = 50, width = 160 ,x = 1220,y = 655)

    root.mainloop()

