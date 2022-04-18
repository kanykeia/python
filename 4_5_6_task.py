# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь)

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class AppError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

class StockError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return self.error


class AddStockError(StockError):
    def __init__(self, text):
        self.text = f'Ошибка добавления на склад товара: \n {text}'


class TransferStockError(StockError):
    def __init__(self, text):
        self.text = f'Ошибка передачи товара: \n {text}'


class OfficeEqStock():
    def __init__(self):
        self.__stock = []

    def add(self, item: 'OfficeEquipment'):
        if not isinstance(item, OfficeEquipment):
            raise AddStockError(f'{item} не относится к оргтехнике')

        self.__stock.append(item)

    def transfer(self, index: int, department: str):
        if not isinstance(index, int):
            raise TransferStockError(f'Недопустимый тип: "{type(index)}"')

        item: OfficeEquipment = self.__stock[index]

        if item.department:
            raise TransferStockError(f'Оборудование {item} уже закреплено за отделом {item.department}')

        item.department = department

    def check(self, **kwargs):
        for index, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield index, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__stock[key]

    def __delitem__(self, key):

        if not isinstance(key, int):
            raise TypeError

        del self.__stock[key]

    def __iter__(self):
        return self.__stock.__iter__()

    def __str__(self):
        return f"На складе сейчас  {len(self.__stock)} оборудования"


class OfficeEquipment():
    transport_rate = 1.17
    wholsale_rate = 1.3
    retale_rate = 1.5
    bonus = 0.95

    def __init__(self, eq_type: str, manufactorer: str, model: str, color: str, purchase_price: float):
        self.eq_type = eq_type
        self.manufactorer = manufactorer
        self.model = model
        self.purchase_price = purchase_price
        self.color = color
        self.printable = True if self.eq_type in ('printer', 'xerox') else False
        self.scannable = True if self.eq_type in ('scanner', 'xerox') else False

        self.department = None

    @property
    def wholesale_price(self):
        return self.purchase_price * self.transport_rate * self.wholsale_rate

    def retale_price(self):
        self.wholesale_price * self.retale_rate

    def __str__(self):
        return f'{self.eq_type} {self.manufactorer} {self.model} {self.color}'


class Printer(OfficeEquipment):
    printable = True
    scannable = False

    def __init__(self, *args):
        super().__init__('printer', *args)


class Scanner(OfficeEquipment):
    printable = False
    scannable = True

    def __init__(self, *args):
        super().__init__('scanner', *args)


class Xerox(OfficeEquipment):
    printable = True
    scannable = True

    def __init__(self, *args):
        super().__init__('xerox', *args)


if __name__ == '__main__':
    stock = OfficeEqStock()
    stock.add(Printer('Canon', 'UF150', 'white', 3000))
    stock.add(Scanner('Epson', 'A200', 'black', 5000))
    stock.add(Xerox('Xerox', 'E300', 'grey', 4000))
    eq_1 = Printer('Canon', 'UF150', 'white', 3000)
    print(stock)

    last_index = None
    for index, itm in stock.check(department=None):
        print(index, itm)
        last_index = index

    print("Передаем 1 устройство")
    stock.transfer(last_index, 'Отдел Розничных продаж')

    for index, itm in stock.check(department=None):
        print(index, itm)

    print(stock)
    print("Удаляем 1 устройство")
    del stock[last_index]
    print(stock)




