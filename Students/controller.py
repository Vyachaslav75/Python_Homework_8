import view as v
import action as a
import generate_students as gs
import work_file as imp_exp

students = {}


def start():
    while True:
        flag = v.user_interface()
        if flag == '1':
            a.new_student()
        elif flag == '2':
            a.new_subj()
        elif flag == '3':
            a.new_mark()
        elif flag == '4':
            a.show_students()
        elif flag == '5':
            a.show_marks()
        elif flag == '6':
            a.stud_mid_subj()
        elif flag == '7':
            a.school_mid_subj()
        elif flag == '8':
            a.stud_medal()
        elif flag == '9':
            gs.generate_school()
        elif flag == '10':
            imp_exp.export_file(students)
        elif flag == '11':
            imp_exp.import_file(students)
        elif flag == '12':
            break
