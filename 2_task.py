# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
class Road:
    _length = None
    _width = None
    def asphalt(self, _length, _width, asp_kg = 25, thickness = 5):
        self._length = _length
        self._width = _width
        self.asp_kg = asp_kg
        self.thickness = thickness
        print(f'Вам необходимо: {_length}м * {_width}м * {asp_kg}кг / 1000 * {thickness}см = {_length * _width * asp_kg / 1000 * thickness} тонн асфальта')

calc = Road()
calc.asphalt(5000, 20)

