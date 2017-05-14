from tkinter import *
from trysql import *


def d_i_t():

    def fbi():
        spsk = reader.get()
        find_for_ill(spsk)
        button_clicked()

    def button_clicked():
        msk = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        atributes = ["#Больного", "Фамилия", "Имя", "Отчество", "Индекс данных", "#донора", "Группа крови",
                     "Резус-фактор", "Дата рождения", "Пол", "Место работы", "Кол-во сдач", "Последняя сдача",
                     "Согласие"]
        arr = find_for_ill(reader.get())
        for ind in range(14):
            spsk = []
            for j in range(min(10, len(arr))):
                spsk.append(str(arr[j][msk[ind]]))
            string = atributes[ind] + "\n" + "\n".join(spsk)
            a[ind].configure(text=string)

    root = Tk()
    root["bg"] = "green"
    root.state("zoomed")
    root.title("Река жизни - доноры по больному")

    informator = Label(root)
    informator.configure(text="Введите ФИО болного.Пример: Иванов Иван Иванович", font="Arial 20")
    informator.place(height=50, width=1380, x=0, y=0)

    reader = Entry(root)
    reader.configure(font="Arial 20")
    reader.place(height=50, width=1220, x=0, y=50)

    button_search = Button(root)
    button_search.configure(text="Искать", command=fbi)
    button_search.place(height=50, width=160, x=1220, y=50)

    a = []
    for i in range(14):
        a.append(Label(root))
        a[i].pack(side='left')

    root.mainloop()
