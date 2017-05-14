from tkinter import *
from trysql import *
from code_window import *

vill_offs = 0

def ill_obsrerve():
    a = recount()
    numill = a[0]
    numdon = a[1]
    numpers = a[2]
    size = numill
    print(size)

    def next():
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
        size = len(arr)
        msk = [5, 1, 2, 3, 4, 7, 8, 9, 10]
        atributes = ["#Больного", "Фамилия", "Имя", "Отчество", "Индекс данных", "Группа крови", "Резус-фактор",
            "Заболевание", "Требуемый объем"]
        try:
            for i in range(9):
                spsk = []
                for j in range(min(15,size)):
                    spsk.append(str(arr[j][msk[i]]))
                string = atributes[i] + "\n" + "\n".join(spsk)
                a[i].configure(text=string)
        except:
            print("Ничего страшного")

    def search_button_clicked():
        global find_offs
        find_offs = 0
        build()

    root = Tk()
    root["bg"] = "green"
    root.state("zoomed")
    root.title("Река жизни - просмотр больных")

    a = []
    #labelinfo  = Label(root)
    for i in range(9):
        a.append(Label(root))
        a[i].pack(side = 'left')

    button_next = Button(root)
    button_next.configure(text="Следующие", command=next)
    button_next.place(height = 40, width = 160 , x = 1220, y = 140)

    button_prev = Button(root)
    button_prev.configure(text="Предыдущие", command=prev)
    button_prev.place(height = 40, width = 160 , x = 1220, y = 100)

    contact_button = Button(root)
    contact_button.configure(text="Получить контакты", command = contact_window)
    contact_button.place(height = 40, width = 160 , x = 1220, y = 0)

    build()
    root.mainloop()

