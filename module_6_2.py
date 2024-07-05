from colorama import Fore, init

init(autoreset=True)


class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, _color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self._color = _color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self._color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(Fore.GREEN + self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self._color = new_color
        else:
            print(Fore.YELLOW + f'Невозможно покрасить в {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()  # Изначальные свойства
vehicle1.set_color('Pink')
vehicle1.set_color('black')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
