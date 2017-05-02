from tkinter import *
from trysql import *
import time
def write_stat():
    global a
    msk = [2, 1, 0]
    atributes = ["Предприятие","Число доноров","Число сдач"]
    for i in range(3):
        a[i].configure(text = atributes[i] + "\n" + statistics(msk[i]))

root = Tk()
root["bg"] = "green"
#root.state("zoomed")
root.title("Река жизни - статистика по предприятиям")

a = []
#labelinfo  = Label(root)
for i in range(3):
    a.append(Label(root,font = 'Arial 20'))
    a[i].pack(side = 'left')

write_stat()

root.mainloop()
