# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionError(Exception):
    error = 'Делить на 0 нельзя!'

    def __str__(self):
        return self.error

class Division(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise DivisionError

        return Division(float(self) / float(other))

if __name__ == '__main__':
    while True:
        try:
            divident, divider = map(Division, input('Введите делимое и делитель через пробел: ').split())
            print(divident / divider)
        except DivisionError as e:
            print(e)
        except ValueError as e:
            print(e)
            break

