from tkinter import *
from trysql import *
from add_donor import *
from finder_graph import *
from statistiks import *
from vatch_ill import *
from donor_ill_table import *

init()
def addition_d():
    adding_person(1)

def addition_i():
    adding_person(0)

main_menu=Tk()
main_menu.title("Река жизни - главное меню")
shw_stat = Button(text = 'Показать статистику по предприятиям',font = "Arial 20")
shw_stat.configure(command  = show_statistics)
shw_stat.pack(fill = "x")

add_dnr = Button(text = 'Добавить больного',font = "Arial 20")
add_dnr.configure(command  = addition_i)
add_dnr.pack(fill = "x")

add_dnr = Button(text = 'Добавить донора',font = "Arial 20")
add_dnr.configure(command  = addition_d)
add_dnr.pack(fill = "x")

fnd_dnr = Button(text = 'Найти донора',font = "Arial 20")
fnd_dnr.configure(command  = finder_donors)
fnd_dnr.pack(fill = "x")

illob = Button(text = 'Просмотр больных',font = "Arial 20")
illob.configure(command  = ill_obsrerve)
illob.pack(fill = "x")

illob = Button(text = 'Согласия доноров по данному больному',font = "Arial 20")
illob.configure(command  = d_i_t)
illob.pack(fill = "x")


main_menu.mainloop()
