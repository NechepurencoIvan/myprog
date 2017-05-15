from tkinter import *
from trysql import *

vill_offs = 0


def ill_obsrerve():
    a = recount()
    numb = a[0]
    size = numb

    def button_cd_clicked():
        c = reader_cd.get()
        j = get_cd(c)
        reader_cd.delete(0, 'end')
        reader_cd.insert(0, str(j))

    def nxt():
        global vill_offs
        if vill_offs + 5 < size:
            vill_offs += 5
            build()

    def prev():
        global vill_offs
        if vill_offs >= 5:
            vill_offs -= 5
        build()

    def build():
        arr = table_ill(vill_offs)
        siz = len(arr)
        msk = [5, 1, 2, 3, 4, 7, 8, 9, 10]
        atributes = ["#Больного", "Фамилия", "Имя", "Отчество", "Индекс данных", "Группа крови", "Резус-фактор",
                     "Заболевание", "Требуемый объем"]

        for ind in range(9):
            spsk = []
            for j in range(min(25, siz)):
                spsk.append(str(arr[j][msk[ind]]))
                if(j >= len(arr)):
                    print()
            string = atributes[ind] + "\n" + "\n".join(spsk)
            a[ind].configure(text=string)

    root = Tk()
    root["bg"] = "green"
    root.state("zoomed")
    root.title("Река жизни - просмотр больных")

    a = []
    for i in range(9):
        a.append(Label(root, bg='green', font="Arial 14"))
        a[i].pack(side='left')

    button_next = Button(root)
    button_next.configure(text="Следующие", command=nxt)
    button_next.place(height=50, width=160, x=1220, y=140)

    button_prev = Button(root)
    button_prev.configure(text="Предыдущие", command=prev)
    button_prev.place(height=50, width=160, x=1220, y=100)

    contact_button = Button(root)
    contact_button.configure(text="Получить контакты", command=button_cd_clicked)
    contact_button.place(height=50, width=160, x=1220, y=0)

    reader_cd = Entry(root)
    reader_cd.configure(font="Arial 20")
    reader_cd.place(height=50, width=700, x=0, y=0)

    build()
    root.mainloop()
