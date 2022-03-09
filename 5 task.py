# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2]

my_list = [8, 7, 7, 5, 2, 2, 1]
print(f'Рейтинг: {my_list}')
# print(max(my_list))
user_number = int(input("Введите число для добавления в рейтинг: "))

while user_number != max(my_list):
    for i in range(len(my_list)):
        if my_list[i] == user_number:
            my_list.insert(i + 1, user_number)
            break

        elif my_list[0] < user_number:
            my_list.insert(0, user_number)
        elif my_list[-1] > user_number:
            my_list.append(user_number)
        elif my_list[i] > user_number > my_list[i + 1]:
            my_list.insert(i + 1, user_number)
    print(f'Новый рейтинг: {my_list}')
    user_number = int(input("Введите число для добавления в рейтинг: "))
