import sqlite3
import random
from try_codification import *

numpers = 0
numdon = 0
numill = 0
bolnoy = ''


def rand_gen():
    zaproses = open('zaproses.sql', 'r')
    for line in zaproses:
        cursor.execute(line)
    zaproses.close()


def randstuff():
    return"randomname_randomnamovich@mail.ru +79536661313"


def get_cd(num):
    cursor.execute("SELECT hash FROM hashes WHERE contact_id = \'" + num + "\'")
    a = cursor.fetchall()
    if len(a) == 0:
        return randstuff()
    p = a[0][0].replace('\\\'', '\'').replace('\'\'', '\"').replace('\\\\', '\\')
    return decodificate(p)


def don_ill_link_add(args):
    cursor.execute("INSERT INTO donors_ill (donor_id , ill_id , confirm ) "
                   "VALUES (\'" + str(args[1]) + "\', \'" + str(args[0]) + "\', \'" + str(args[2]) + "\');")


def search_ill_by_name(spisk):
    cursor.execute("SELECT ill.ill_id FROM ill, persons WHERE ill.person_id = persons.person_id AND persons.fam = \'"
                   + spisk[0] + "\' AND persons.name = \'" + spisk[1] + "\' AND persons.otch = \'" + spisk[2] + "\'")
    tbl = cursor.fetchall()
    return tbl[0][0]


def table_ill(propusk):
    cursor.execute("SELECT * FROM persons, ill WHERE persons.person_id = ill.person_id LIMIT 25 OFFSET " + str(propusk))
    return cursor.fetchall()


def debug_table(string):
    cursor.execute(string)
    results = cursor.fetchall()
    for i in results:
        print(i)


def show_donors(col):
    cursor.execute("SELECT * FROM persons, donors WHERE persons.person_id = donors.person_id")
    results = cursor.fetchall()
    a = []
    for i in results:
        a.append(str(i)[col])
    return '\n'.join(a)


def find_by_ill(string):
    mylist = string.split()
    zapr = "SELECT ill.bllood_gr, ill.rf FROM persons, ill WHERE ill.person_id = persons.person_id " \
           "AND persons.fam = \'" + mylist[0] + "\' AND persons.name = \'" + mylist[1] + "\' AND persons.otch = \'"\
           + mylist[2] + "\' LIMIT 1"
    cursor.execute(zapr)
    results = cursor.fetchall()
    return results


def find_for_ill(string):
    mylist = string.split()
    zapr = "SELECT ill.ill_id, ill.bllood_gr, ill.rf FROM persons, ill WHERE ill.person_id = persons.person_id " \
           "AND persons.fam = \'" + mylist[0] + "\' AND persons.name = \'" + mylist[1] + "\' AND persons.otch = \'"\
           + mylist[2] + "\' LIMIT 1"
    cursor.execute(zapr)
    results = cursor.fetchall()
    if results == []:
        return [("Не найдено", "Не найдено", "Не найдено", "Не найдено", "Не найдено", "Не найдено", "Не найдено",
                 "Не найдено", "Не найдено", "Не найдено", "Не найдено", "Не найдено", "Не найдено",
                 "Не найдено", "Не найдено")]
    results1 = results[0][0]
    blgr = results[0][1]
    rf = results[0][2]
    cursor.execute("SELECT persons.*, donors.*, donors_ill.confirm FROM persons, donors, donors_ill "
                   "WHERE persons.person_id = donors.person_id AND donors.donor_id = donors_ill.donor_id "
                   "AND donors_ill.ill_id = \'" + str(results1) + "\' AND donors.bllood_gr = \'" + str(blgr) +
                   '\' AND donors.rf = \'' + str(rf) + '\'')
    results2 = cursor.fetchall()
    return results2


def find_donors(blgr, rf, ofs, col):
    string = "SELECT * FROM persons, donors WHERE persons.person_id = donors.person_id AND donors.rf = " + \
        str(rf) + " AND donors.bllood_gr = " + str(blgr) + " LIMIT 25 OFFSET " + str(ofs)
    cursor.execute(string)
    results = cursor.fetchall()
    a = []
    for i in results:
        a.append(str(i[col]))
    return '\n'.join(a)


def statistics(col):
    cursor.execute('SELECT sum(passed) AS itogo, count(person_id) AS ludey, work FROM donors '
                   'GROUP BY work ORDER BY itogo DESC')
    results = cursor.fetchall()
    a = []
    for i in results:
        a.append(str(i[col]))
    return '\n'.join(a)


def info():
    a = ["На настоящий момент в базе", str(numpers), "человек:", str(numdon), "донор(ов) и", str(numill), "больных(ой)"]
    return ' '.join(a)


def addpers(string, cd):
    global numpers
    mylist = string.split()
    fam = mylist[0]
    nam = mylist[1]
    otch = mylist[2]
    cont = cd
    c = "INSERT INTO persons (person_id, fam, name, otch, contact_id) VALUES ('" + str(numpers) + "', '" + fam + "','" \
        + nam + "','" + otch + "','" + str(cont) + "');"
    cursor.execute(c)


def trsqladdon(string):
    global numdon, numpers
    mylist = string.split()
    numdon += 1
    numpers += 1
    d_id = str(numdon)
    p_id = str(numpers)
    blgr = mylist[0]
    rf = mylist[1]
    born = mylist[2]
    sex = mylist[3]
    wpl = mylist[4]
    passed = mylist[5]
    passed_lst = mylist[6]
    string = 'INSERT INTO donors (donor_id, person_id, bllood_gr, rf, born, sex, work, passed, lastpass) VALUES (\'' + \
        d_id + '\', \'' + p_id + '\',\'' + blgr + '\',\'' + rf + '\',\'' + born + '\',\'' + sex + '\',\'' + wpl\
             + '\',\'' + passed + '\',\'' + passed_lst + '\');\n'
    cursor.execute(string)


def trsqladdill(string):
    global numill, numpers
    numill += 1
    numpers += 1
    mylist = string.split()
    ill_id = str(numill)
    p_id = str(numpers)
    blgr = mylist[0]
    rf = mylist[1]
    dis = mylist[2]
    vol = mylist[3]
    string = 'INSERT INTO ill (ill_id, person_id, bllood_gr ,rf, disease,volume) VALUES (\'' + \
        ill_id + '\', \'' + p_id + '\',\'' + blgr + '\',\'' + rf + '\',\'' + dis + '\',\'' + vol + '\');\n'
    cursor.execute(string)


def init():
    global numpers, numdon, numill, conn, cursor
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
#    DDL = open('creation2.sql')
#    for line in DDL:
#        print(line)
#        cursor.execute(line)
    rand_gen()
    cursor.execute('SELECT * FROM hashes')
    cursor.execute("SELECT count(person_id) FROM persons")
    results = cursor.fetchall()
    numpers = int(results[0][0])
    cursor.execute("SELECT count(donor_id) FROM donors")
    results = cursor.fetchall()
    numdon = int(results[0][0])
    cursor.execute("SELECT count(ill_id) FROM ill")
    results = cursor.fetchall()
    numill = int(results[0][0])
    return[numill, numdon, numpers]


def recount():
    cursor.execute("SELECT max(person_id) FROM persons")
    results = cursor.fetchall()
    numpers = int(results[0][0])
    cursor.execute("SELECT max(donor_id) FROM donors")
    results = cursor.fetchall()
    numdon = int(results[0][0])
    cursor.execute("SELECT max(ill_id) FROM ill")
    results = cursor.fetchall()
    numill = int(results[0][0])
    return[numill, numdon, numpers]


def get_unused_ncd():
    cursor.execute("SELECT contact_id FROM hashes")
    used_cd = cursor.fetchall()
    cd = str(random.randint(0, 10000))
    while (cd) in used_cd:
        cd = str(random.randint(0, 10000))
    return cd


def ya_ustal_pridumivat_imena_functiyam(cd, non_coded):
    for_cntct_str = codificate(non_coded).replace('\\', '\\\\').replace('\"', '\'\'').replace('\'', '\\\'')
    cursor.execute('INSERT INTO hashes (contact_id, hash) VALUES (\'' + cd + '\', \"' + for_cntct_str + '\")')
