from tkinter import *
from trysql import *

vill_offs = 0
def ill_obsrerve():

    def next():
        global vill_offs
        vill_offs += 1
        built()

    def prev():
        global vill_offs
        if vill_offs > 0:
            vill_offs -= 1
        built()

    def built():
        arr = table_ill(vill_offs)
        print(arr)
        msk = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        atributes = ["#Больного", "Фамилия", "Имя", "Отчество", "Индекс данных", "Группа крови", "Резус-фактор",
            "Заболевание", "Требуемый объем"]
        try:
            for i in range(9):
                spsk = []
                for j in range(5):
                    spsk.append(str(arr[j][msk[i]]))
                print(spsk)
                string = atributes[i] + "\n" + "\n".join(spsk)
                a[i].configure(text=string)
        except:
            print("Ничего страшного")

    def search_button_clicked():
        global find_offs
        find_offs = 0
        built()

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

    built()
    root.mainloop()

