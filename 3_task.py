# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32
from statistics import mean

with open('text_3.txt', 'r', encoding='UTF-8') as file:

    employees_dict = {line.split()[0]: float(line.split()[1]) for line in file}
    # print(employees_dict)
    print(f'Сотрудники которые получают зп меньше 20k:')
    for employer, salary in employees_dict.items():
        if salary < 20000:
            print(employer)
print(f'\nСредняя величина дохода сотрудников равна: {round(mean(list(employees_dict.values())),2)}')


