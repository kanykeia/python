# 1-task
name = input("Как к вам обращаться? ")
print("Добрый день,", name, "!")
age = int(input("Сколько Вам лет?"))
print("Рады с Вами познакомиться,", name, ", которому", age, "лет!")
animal = input("Ваше любимое животное?")
print(f"{animal}-отличный выбор!")

# 2-task
time = int(input("Enter your time in seconds"))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f"{hours:2}:{minutes:02}:{seconds:02}")

# 3-task
n = input("Введите любую цифру")
while n < '0':
    print("Введите целую цифру, которая больше 0. Попробуйте еще раз, пожалуйста.")
    break
#n = input("Введите любую целую цифру больше 0: ")
print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

# 4-task
num_1 = int(input("Введите, пожалуйста,целое положительное число "))
greatest_dig = 0
num = num_1

while num > 0:
    dig = num % 10
    if dig > greatest_dig:
        greatest_dig = dig
        if greatest_dig == 9:
            break
    num = num // 10

print(f'Наибольшая цифра в числе {num_1} равна {greatest_dig}')

# 5-6-tasks
costs = float(input("Введите, пожалуйста, значение издержек Вашей фирмы."))
revenue = float(input("Отлично! Теперь введите значение выручки Вашей фирмы!"))

if costs < revenue:
    print(f"Поздравляю! Вы работаете с прибылью{revenue - costs}")
    print(f"Рентабельность вашей выручки составила:{(revenue - costs)/revenue*100:1f}")
    personal = int(input("А сколько человек работает в вашей фирме?"))
    print(f"Если раздадите прибыль Вашим сотрудник, то каждый из них получит: {(revenue - costs)/personal:1f}")
elif costs == revenue:
    print("Вы не получаете прибыль, но у вас и нет убытка!")
else:
    print(f"Увы, Вы работаете в убыток на {(revenue - costs)*-1}")

# 6-task
while True:
    days = 1
    a = float(input("Добрый день! Подскажите Ваш результат на первой пробежке!"))
    b = float(input("Какого результата Вы хотите добиться?"
                " И мы подскажем на какой день можно будет достичь его при увеличении нагрузки на 10% каждый день ;)"))
    if a <= 0 or b < 0:
         print("Результат должен быть больше нуля. Стартовое значение больше или равно нулю")
    else:
        while a < b:
         a += a * 0.1
        days += a * 0.1
    print(f"Вы добьетесь результата за {int(days)} дней")
    break