# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date():
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def reformat(cls, day_month_year):
        new_date = []

        for i in day_month_year.split('-'):
            new_date.append(i)

        return int(new_date[0]), int(new_date[1]), int(new_date[2])

    @staticmethod
    def validate(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2022:
                    return 'Данные верны'
                else:
                    return 'Неверно ввели год'
            else:
                return "Неверно ввели месяц"
        else:
            return "Неверно ввели число"
    def __str__(self):
        return f'Текущая дата {Date.reformat(self.day_month_year)}'


today = Date('14-04-2022')
print(today)
print(Date.validate(14, 4, 2022))
print(today.validate(32, 4, 2022))
print(Date.reformat('14-04-2022'))
print(today.reformat('14-04-2022'))





