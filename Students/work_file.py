def export_file(data, file_name='school.txt'):
    with open(file_name, 'w', encoding='utf8') as file:
        # file.write('\n' + ', '.join(data))
        for key in data:
            file.write(f'{key}'+'\n')
            for key_subj in data[key]:
                marks = [str(x) for x in data[key][key_subj]]
                if len(marks) > 0:
                    marks = ', '.join(marks)
                else:
                    marks = 'нет'
                file.write(f'{key_subj}, {marks}'+'\n')
            file.write('\n')


def import_file(data, file_name='school.txt'):
    with open(file_name, 'r', encoding='utf8') as file:
        name = ''
        for line in file:
            if line != '\n':
                res = [x for x in line.rstrip().split(', ')]
                if len(res) == 1:
                    name = res[0]
                    data[name] = {}
                else:
                    res = [x for x in line.rstrip().split(', ')]
                    if res[1] == 'нет':
                        data[name][res[0]] = []
                    else:
                        data[name][res[0]] = [int(x) for x in res[1:]]
