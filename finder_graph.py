from tkinter import *
from trysql import *


find_rf = 0
find_acc = 0
find_offs = 0


def finder_donors():
    def nxt():
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
        if not find_rf == results[0][1]:
            ch_rf()
        listbox_blgr.select_set(results[0][0] - 1)
        search_button_clicked()

    def button_cd_clicked():
        c = reader_cd.get()
        j = get_cd(c)
        reader_cd.delete(0, 'end')
        reader_cd.insert(0, str(j))

    def button_clicked():
        msk = [5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13]
        atributes = ["#донора", "Фамилия", "Имя", "Отчество", "Индекс данных", "#человека", "Группа крови",
                     "Резус-фактор", "Дата рождения", "Пол", "Место работы", "Кол-во сдач", "Последняя сдача"]
#        try:
        p = listbox_blgr.curselection()[0]
        for ind in range(13):
            a[ind].configure(
                 text=atributes[ind] + "\n" + find_donors(int(p) + 1, find_rf, find_offs, msk[ind]))
#        except:
#            print('ничего страшного')

    def search_button_clicked():
        global find_offs
        find_offs = 0
        button_clicked()

    def ch_rf():
        global find_rf
        if find_rf == 0:
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
        if find_acc == 0:
            find_acc = 1
        else:
            find_acc = 0
        button_acc.configure(text=("Согласие: " + getagrfrbool(find_acc)))

    def link():
        string = reader.get()
        arr = search_ill_by_name(string.split())
        spsk = [arr, reader_dnr_id.get(), find_acc]
        don_ill_link_add(spsk)

    root = Tk()
    root["bg"] = "green"
    root.state("zoomed")
    root.title("Река жизни - поиск доноров")

    button = Button(root)
    button.configure(text="Поиск", command=search_button_clicked)
    button.place(height=40, width=160, x=1220, y=400)

    contact_button = Button(root)
    contact_button.configure(text="Получить контакты", command=button_cd_clicked)
    contact_button.place(height=50, width=160, x=1220, y=0)

    button_rf = Button(root)
    button_rf.configure(text=("Резус-фактор: " + str(find_rf)), command=ch_rf)
    button_rf.place(height=40, width=160, x=1220, y=200)

    a = []
    for i in range(13):
        a.append(Label(root, bg='green'))
        a[i].pack(side='left')

    listbox_blgr = Listbox(root, height=4, width=160, selectmode=EXTENDED)
    list_blgr = [1, 2, 3, 4]
    for i in list_blgr:
        listbox_blgr.insert(END, i)
    listbox_blgr.place(x=1220, y=240)

    button_next = Button(root)
    button_next.configure(text="Следующие", command=nxt)
    button_next.place(height=40, width=160, x=1220, y=140)

    button_prev = Button(root)
    button_prev.configure(text="Предыдущие", command=prev)
    button_prev.place(height=40, width=160, x=1220, y=100)

    reader = Entry(root)
    reader.configure(font="Arial 20")
    reader.place(height=50, width=700, x=0, y=655)

    reader_dnr_id = Entry(root)
    reader_dnr_id.configure(font="Arial 20")
    reader_dnr_id.place(height=50, width=50, x=700, y=655)

    button_add_link = Button(root)
    button_add_link.configure(text="Приписать донора", command=link)
    button_add_link.place(height=50, width=160, x=750, y=655)

    informator = Label(root)
    informator.configure(text="Введите ФИО болного.Пример: Иванов Иван Иванович", font="Arial 20")
    informator.place(height=50, width=700, x=0, y=605)

    nd = Label(root)
    nd.configure(text="#д", font="Arial 8")
    nd.place(height=50, width=50, x=700, y=605)

    button_acc = Button(root)
    button_acc.configure(text=("Согласие: " + getagrfrbool(find_rf)), command=ch_acc)
    button_acc.place(height=50, width=160, x=750, y=605)

    button_dnr = Button(root)
    button_dnr.configure(text="Искать", command=fbd)
    button_dnr.place(height=50, width=160, x=1120, y=655)

    reader_cd = Entry(root)
    reader_cd.configure(font="Arial 20")
    reader_cd.place(height=50, width=700, x=0, y=0)


    root.mainloop()

