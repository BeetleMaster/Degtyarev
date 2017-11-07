'''Дан файл с расписанием занятий на неделю.
Помимо названия предмета в нем также указано лекция это, или практическое занятие, или лабораторная работа.
 В одной строке может быть указаны только один предмет с информацией о нем.
 Посчитать, сколько за неделю проходит практических занятий, лекций и лабораторных работ.'''


with open("week.txt", "r") as f:
    data = f.read().split()

lecture = 0
lab = 0
practice = 0
try:
    if not data:
        raise FileNotFoundError("Файл пуст")
except FileNotFoundError as empty:
    print(empty)
else:
    for i in data:
        if i == '(лекц.)':
            lecture += 1
        if i == '(практ.)':
            practice += 1
        if i == '(лаб.)':
            lab += 1

with open("output.txt", "w") as output:
    print("Количество лекций: {}".format(lecture), file = output)
    print("Количество практик: {}".format(practice), file = output)
    print("Количество лабораторных работ: {}".format(lab), file = output)