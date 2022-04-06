# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
import random
with open('text_5.txt', 'w+', encoding='UTF-8') as file:
    file.write(' '.join([str(random.randint(0, 150)) for _ in range(10)]))
    file.seek(0)
    a = sum(map(int, file.readline().split()))
    print(f'Сумма цифр в файле "text_5.txt" равна: {a}')
