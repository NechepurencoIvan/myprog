from tkinter import *
from trysql import *
import time
def button_clicked():
    msk = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13]
    atributes = ["#","Фамилия","Имя","Отчество","Индекс данных","#донора","Группа крови","Резус-фактор","Дата рож"
"дения","Пол","Место работы","Кол-во сдач","Последняя сдача"]
    for i in range(13):
        a[i].configure(text = atributes[i] + "\n" + find_donors(int(listbox_blgr.curselection()[0]) + 1,rf,msk[i]))

def ch_rf():
    global rf
    if(rf == 0):
        rf = 1
    else:
        rf = 0
    button_rf.configure(text = ("Резус-фактор" + str(rf)))

root = Tk()
root["bg"] = "green"
root.state("zoomed")
root.title("Река жизни")


button = Button(root)
button.configure(text="Поиск", command=button_clicked)
button.place(height = 40, width = 160 , x = 1220, y = 600)

rf = 0
button_rf = Button(root)
button_rf.configure(text=("Резус-фактор: " + str(rf)), command=ch_rf)
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


root.mainloop()
