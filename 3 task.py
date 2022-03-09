# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и dict.

winter_list = [12, 1, 2]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]

seasons = {'Зима': winter_list, 'Весна': spring_list, 'Лето': summer_list, 'Осень': autumn_list}

user_mounth = int(input('Введите номер месяца: '))

for key in seasons.keys():
    if user_mounth in seasons[key]:
        print(key)
