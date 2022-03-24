#  Реализовать функцию, принимающую два числа (позиционные аргументы) и
#  выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division():
    global number1, number2
    try:
        number1 = int(input('Введите делимое число: '))
        number2 = int(input('Введите делитель: '))
        return f'Если разделить {number1} на {number2}, то получится:  {number1 / number2}'
    except ZeroDivisionError:
        return ('На нуль делить нельзя!')
print(division())
