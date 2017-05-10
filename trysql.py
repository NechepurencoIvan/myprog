import sqlite3

#DDL = open('creation2.sql')
#for line in DDL:
#    line
#    print(line)
#    cursor.execute(line)

def rand_gen():
    zaproses = open('zaproses.sql')
    for line in zaproses:
        line
        cursor.execute(line)
    zaproses.close()

def don_ill_link_add(args):
    cursor.execute("INSERT INTO donors_ill (donor_id , ill_id , confirm ) "
                   "VALUES (\'" + str(args[0]) + "\', \'" + str(args[1]) + "\', \'" + str(args[2]) + "\');")
    cursor.execute("SELECT * FROM donors_ill")
    print(cursor.fetchall())

def search_ill_by_name(spisk):
    cursor.execute("SELECT ill.ill_id FROM ill, persons WHERE ill.person_id = persons.person_id "
"AND persons.fam = \'" + spisk[0] + "\' AND persons.name = \'" + spisk[1] + "\' AND persons.otch = \'" + spisk[2] + "\'")
    tbl = cursor.fetchall()
    return tbl[0][0]

def table_ill(propusk):
    cursor.execute("SELECT * FROM persons, ill WHERE persons.person_id = ill.person_id LIMIT 20 OFFSET " + str(propusk))
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
"AND persons.fam = \'" + mylist[0] + "\' AND persons.name = \'" + mylist[1] + "\' " \
"AND persons.otch = \'" + mylist[2] + "\' LIMIT 1"
    cursor.execute(zapr)
    results = cursor.fetchall()
    return results

def find_donors(blgr,rf,ofs,col):
    string = "SELECT * FROM persons, donors WHERE persons.person_id = donors.person_id AND donors.rf = " + \
str(rf) + " AND donors.bllood_gr = " + str(blgr) + " LIMIT 40 OFFSET " + str(ofs)
    cursor.execute(string)
    results = cursor.fetchall()
    a = []
    for i in results:
        a.append(str(i[col]))
    return '\n'.join(a)

def show_ills():
    cursor.execute("SELECT * FROM persons, ill WHERE persons.person_id = ill.person_id")
    results = cursor.fetchall()

def statistics(col):
    cursor.execute("SELECT sum(passed) AS itogo, count(person_id) AS ludey, work FROM donors GROUP BY work ORDER BY ito"
"go DESC")
    results = cursor.fetchall()
    a = []
    for i in results:
        a.append(str(i[col]))
    return '\n'.join(a)

def info():
    a = ["На настоящий момент в базе", str(numpers), "человек:", str(numdon), "донор(ов) и", str(numill), "больных(ой)"]
    return ' '.join(a)

def addpers(string):
    global numpers
    numpers += 1
    mylist = string.split()
    fam = mylist[0]
    nam = mylist[1]
    otch = mylist[2]
    cont = int(mylist[3])
    c = "INSERT INTO persons (person_id, fam, name, otch, contact_id) VALUES ('" + str(numpers) + "', '" + fam + "','" \
+ nam + "','" + otch + "','" + str(cont) + "');"
    cursor.execute(c)

def ADDDONOR(string):
    global numdon
    mylist = string.split()
    numdon = numdon + 1
    d_id = str(numdon)
    p_id = str(numpers)
    blgr = mylist[0]
    rf = mylist[1]
    born = mylist[2]
    sex = mylist[3]
    wpl = mylist[4]
    passed = mylist[5]
    passed_lst = mylist[6]
    string = 'INSERT INTO donors (donor_id,person_id,bllood_gr, rf, born, sex, work, passed, lastpass) VALUES (\'' + \
d_id + '\', \'' + p_id + '\',\'' + blgr + '\',\'' + rf + '\',\'' + born + '\',\'' + sex + '\',\'' + wpl + '\',\'' + \
passed + '\',\'' + passed_lst + '\');\n'
    cursor.execute(string)

def ADDILL(string):
    #addpers()
    global numill
    numill = numill + 1
    mylist = string.split()
    ill_id = str(numill)
    p_id = str(numpers)
    blgr = mylist[0]#str(input())
    rf = mylist[1]#str(input())
    dis = mylist[2]#str(input())
    vol = mylist[3]#str(input())
    string = 'INSERT INTO ill (ill_id, person_id, bllood_gr ,rf, disease,volume) VALUES (\'' + \
ill_id + '\', \'' + p_id + '\',\'' + blgr + '\',\'' + rf + '\',\'' + dis + '\',\'' + vol + '\');\n'
    cursor.execute(string)


def init():
    global numpers, numdon, numill,conn,cursor
    numpers = 0
    numdon = 0
    numill = 0
    conn = sqlite3.connect('Chinook_Sqlite.sqlite')
    cursor = conn.cursor()
    rand_gen()
    cursor.execute("SELECT count(person_id) FROM persons")
    results = cursor.fetchall()
    numpers = int(results[0][0])
    cursor.execute("SELECT count(donor_id) FROM donors")
    results = cursor.fetchall()
    numdon = int(results[0][0])
    cursor.execute("SELECT count(ill_id) FROM ill")
    results = cursor.fetchall()
    numill = int(results[0][0])
