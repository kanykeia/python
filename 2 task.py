# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
def info(name=None, surname=None, year=None, city=None, email=None, telephone=None):
    name = input('enter name: ')
    surname = input('enter surname: ')
    year = input('enter year of birth: ')
    city = input('enter living city: ')
    email = input('enter email: ')
    telephone = input('input telephone: ')
    return ' '.join([name, surname, year, city, email, telephone])
print(info())

