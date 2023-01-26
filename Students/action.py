import view as v
import controller as c


def new_student():
    stud = ['Фамилия', 'Имя']
    stud = v.input_data(stud)
    if len(c.students) == 0:
        c.students[' '.join(stud)] = {}
    else:
        key = list(c.students.keys())[0]
        subjs = list(c.students[key])
        c.students[' '.join(stud)] = {}
        for i in subjs:
            c.students[' '.join(stud)][i] = []


def new_subj(subj=''):
    if subj == '':
        subj = v.input_data(['Предмет'])[0]
    for key in c.students:
        c.students[key][subj] = []


def new_mark(stud_name='', subj='', mark=0):
    try:
        if stud_name == '' or subj == '' or mark == 0:
            stud_name = ' '.join(v.input_data(['Фамилия', 'Имя']))
            subj = v.input_data(['Предмет'])[0]
            mark = int(v.input_data([f'{stud_name} оценку по {subj}'])[0])
        c.students[stud_name][subj].append(mark)
    except:
        v.show_data('Неверный ввод')


def show_students():
    for key in c.students:
        v.show_data(key)


def show_marks():
    stud = ' '.join(v.input_data(['Фамилия', 'Имя']))
    try:
        for key in c.students[stud]:
            v.show_data(
                f'{key}, оценки: {", ".join([str(x) for x in c.students[stud][key]])}')
    except:
        v.show_data('Неверный ввод')


def calc_mid(data):
    if len(data) == 0:
        return 0
    return sum(data)/len(data)


def stud_mid_subj():
    stud = ' '.join(v.input_data(['Фамилия', 'Имя']))
    subj = v.input_data(['Предмет'])[0]
    try:
        mid = calc_mid(c.students[stud][subj])
        v.show_data(f'{subj}, средний балл= {mid}')
    except:
        v.show_data('Неверный ввод')


def school_mid_subj():
    subj = v.input_data(['Предмет'])[0]
    mid = 0
    try:
        for key in c.students:
            mid += calc_mid(c.students[key][subj])
        v.show_data(f'{subj}, средний балл по школе {mid/len(c.students)}')
    except:
        v.show_data('Неверный ввод')


def check_mark(data):
    flag = True
    for i in data:
        if i < 4:
            flag = False
            break
    return flag


def stud_medal():
    medal_list = []
    for key in c.students:
        for key_subj in c.students[key]:
            if not check_mark(c.students[key][key_subj]):
                break
        else:
            medal_list.append(key)
    v.show_data(f'Медалисты: {", ".join(medal_list)}')
