from tkinter import *
from trysql import *
from add_donor import *
from finder_graph import *
from statistiks import *

init()
def addition_d():
    adding_person(1)

def addition_i():
    adding_person(0)

main_menu=Tk()
main_menu.title("Река жизни - главное меню")
shw_stat = Button(text = 'Показать статистику по предприятиям')
shw_stat.configure(command  = show_statistics)
shw_stat.pack()

add_dnr = Button(text = 'Добавить больного')
add_dnr.configure(command  = addition_i)
add_dnr.pack()

add_dnr = Button(text = 'Добавить донора')
add_dnr.configure(command  = addition_d)
add_dnr.pack()

fnd_dnr = Button(text = 'Найти донора')
fnd_dnr.configure(command  = finder_donors)
fnd_dnr.pack()

main_menu.mainloop()
