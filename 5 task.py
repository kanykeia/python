# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу

def sum_num(number=None):
    final_sum = 0
    end = False
    while end == False:
        number = input('Введите цифры через пробел для вывода суммы или любой другой знак для выхода: ').split()
        int_sum = 0
        for el in range(len(number)):
            if number[el].isdigit():
                int_sum = int_sum + int(number[el])
            else:
                end = True
                break
        final_sum = final_sum + int_sum
        print (f'Текущая сумма равна {final_sum}')
    return (f'Итоговая сумма равна {final_sum}')


print(sum_num())
