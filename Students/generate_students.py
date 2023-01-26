import controller as c
import random
import action as a


def generate_school():
    generate_students()
    generate_subjects()
    generate_marks()


def generate_students():
    firs_names = [
        ['Иван', 'Петр', 'Сидор', 'Никита', 'Ахмед',
            'Андрей', 'Михаил', 'Григорий', 'Мансур', 'Артем'],
        ['Елена', 'Динара', 'Ольга', 'Зинаида', 'София', 'Алина',
         'Ангелина', 'Изаура', 'Зоя', 'Татьяна']]
    last_names = [
        ['Иванов', 'Петров', 'Сидоров', 'Зайцев', 'Волков',
            'Рябов', 'Мухин', 'Зуев', 'Лапин', 'Осипов'],
        ['Егорова', 'Боброва', 'Зыкова', 'Зимина', 'Белова', 'Котова',
         'Савина', 'Турова', 'Титова', 'Носова']]
    for i in range(100):
        gender = random.randint(0, 1)
        firs_name = random.randint(0, 9)
        last_name = random.randint(0, 9)
        c.students[' '.join([last_names[gender][last_name],
                            firs_names[gender][firs_name]])] = {}


def generate_subjects():
    subjects = ['Физика', 'Химия', 'Биология',
                'Математика', 'Физкультура', 'История']
    for i in subjects:
        a.new_subj(subj=i)


def generate_marks():
    for i in c.students:
        medal = random.randint(0, 1)
        for j in c.students[i]:
            for k in range(5):
                if medal:
                    mark = random.randint(4, 5)
                else:
                    mark = random.randint(1, 5)
                a.new_mark(i, j, mark)
