from tkinter import *
from trysql import *


def show_statistics():
    st_a = []
    root_st = Tk()
    root_st["bg"] = "green"
    root_st.title("Река жизни - статистика по предприятиям")
    msk = [2, 1, 0]
    atributes = ["Предприятие", "Число доноров", "Число сдач"]
    for i in range(3):
        st_a.append(Label(root_st, font='Arial 20', text=atributes[i] + "\n" + statistics(msk[i])))
        st_a[i].pack(side='left')
    root_st.mainloop()
