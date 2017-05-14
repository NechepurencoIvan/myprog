import random
from try_codification import *

names_m = ['Ivan', 'Semen', 'Andrew', 'Alexandr', 'Peter', 'Mark', 'Kirill', 'Stepan', 'Oleg', 'Igor', 'Maksim']
families_m = ['Ivanov', 'Semenov', 'Andreev', 'Alexandrov', 'Petrov', 'Serov', 'Mixaylov', 'Nechepurenco', 'Mesherykov',
              'Sobakin', 'Pheophanov', 'Bogomol', 'Molchanov', 'Anisimov', 'Shavrin', 'Kalgushkin', 'Mixaylov',
              'Liferenko', 'Marchenko', 'Roslovtsev', 'Zhukovskiy']
otshestvs_m = ['Ivanovich', 'Semenovich', 'Andreevich', 'Alexandrovich', 'Petrovich', 'Markovich', 'Kirillovich',
               'Stepanovich', 'Olegovich', 'Igorevich', 'Maksimovich']
names_fm = ['Maria', 'Sophiya', 'Anna', 'Elena', 'Galina', 'Irina', 'Svetlana', 'Inna', 'Polina']
families_fm = ['Ivanova', 'Semenova', 'Andreeva', 'Alexandrova', 'Petrova', 'Serova', 'Mixaylova', 'Nechepurenco',
               'Mesherykova', 'Sobakina', 'Pheophanova', 'Bogomol', 'Molchanova', 'Anisimova', 'Shavrina',
               'Kalgushkina', 'Mixaylova', 'Liferenko', 'Marchenko', 'Roslovtseva', 'Zhukovskaya']
otshestvs_fm = ['Ivanovna', 'Semenovna', 'Andreevna', 'Alexandrovna', 'Peterovna', 'Markovina', 'Kirillovna',
                'Stepanovna', 'Olegovna', 'Igorevna', 'Maksimovna']
desiases = ['hemopfilia', 'anemia', 'injuries', 'other', 'vampirism']
sexes = ['man', 'woman']
works = ['RNPC', 'teacher', 'deputate', 'non-working', 'student', 'driver']
bldgrps = [1, 2, 3, 4]
resfacts = [0, 1]
days = ['01', '05', '08', '14', '17', '20', '25']
months = ['01', '03', '6', '9', '11']

contacts = ['someeamail@mail.ru 367363', '253-625', 'jdjkdcddfk', 'somebody_once_told_me@google.com',
            'www.leningrad.ru', 'I\'m bored to invent names', '8-800-555-35-35', '241-141 gruzomviki',
            'mladshiyleytenantt@malchik.molodoy', 'anotherfake@fakes.ru']

zaproses = open("zaproses.sql", "w")

no_persons = 0
no_donors = 0
no_ill = 0
a = 0
used_cd = []
dons_blood = []


def get_rand_dateb():
    return str(random.randint(1960, 1998)) + '-' + str(random.choice(months)) + '-' + str(random.choice(days))


def get_rand_datep():
    return str(random.randint(2007, 2017)) + '-' + str(random.choice(months)) + '-' + str(random.choice(days))


def addpersons(sex):
    global no_persons
    no_persons += 1
    p_id = str(no_persons)
    if sex:
        p_fam = random.choice(families_m)
        p_nam = random.choice(names_m)
        p_otch = random.choice(otshestvs_m)
    else:
        p_fam = random.choice(families_fm)
        p_nam = random.choice(names_fm)
        p_otch = random.choice(otshestvs_fm)
    cd = str(random.randint(0, 10000))
    while cd in used_cd:
        cd = str(random.randint(0, 10000))
    used_cd.append(cd)
    for_cntct_str = codificate(random.choice(contacts)).replace('\\', '\\\\').replace('\"', '\'\'').\
        replace('\'', '\\\'')
    string = 'INSERT INTO hashes (contact_id, hash) VALUES (\'' + cd + '\', \"' + for_cntct_str + '\");\n'
    zaproses.write(string)
    string = 'INSERT INTO persons (person_id, fam, name, otch, contact_id) VALUES (\'' + p_id + '\', \'' + p_fam + \
        '\',\'' + p_nam + '\',\'' + p_otch + '\',\'' + cd + '\');\n'
    zaproses.write(string)


def adddonor():
    global no_donors
    no_donors += 1
    d_id = str(no_donors)
    p_id = str(no_persons + 1)
    blgr = str(random.choice(bldgrps))
    rf = str(random.choice(resfacts))
    born = get_rand_dateb()
    sex = random.choice(sexes)
    wpl = random.choice(works)
    passed = str(random.randint(0, 40))
    passed_lst = (get_rand_datep())
    if sex == 'man':
        addpersons(1)
    else:
        addpersons(0)
    string = 'INSERT INTO donors (donor_id,person_id,bllood_gr, rf, born, sex, work, passed, lastpass) VALUES (\'' \
             + d_id + '\', \'' + p_id + '\',\'' + blgr + '\',\'' + rf + '\',\'' + born + '\',\'' + sex + '\',\'' + wpl \
             + '\',\'' + passed + '\',\'' + passed_lst + '\');\n'
    zaproses.write(string)


def addill():
    global no_ill
    no_ill = no_ill + 1
    ill_id = str(no_ill)
    p_id = str(no_persons + 1)
    blgr = str(random.choice(bldgrps))
    rf = str(random.choice(resfacts))
    dis = random.choice(desiases)
    vol = str(random.randint(1, 4))
    addpersons(random.randint(0, 1))
    string = 'INSERT INTO ill (ill_id, person_id, bllood_gr ,rf, disease,volume) VALUES (\'' + ill_id + '\', \'' + \
             p_id + '\',\'' + blgr + '\',\'' + rf + '\',\'' + dis + '\',\'' + vol + '\');\n'
    zaproses.write(string)

for i in range(120):
    adddonor()
for i in range(60):
    addill()
for i in range(120):
    adddonor()
for i in range(60):
    addill()

another_spisok = []
for i in range(500):
    a = str(random.randint(1, 241))
    b = str(random.randint(1, 121))
    if not (a,b) in another_spisok:
        another_spisok.append((a,b))
        zaproses.write('INSERT INTO donors_ill (donor_id, ill_id, confirm) VALUES (\'' + a +
                       '\', \'' + b + '\', \'' + str(random.randint(0, 1)) + '\');\n')

zaproses.close()