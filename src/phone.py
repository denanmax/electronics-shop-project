from src.item import Item

class Phone(Item):
    """Инициализатор содержит все атрибуты класса Item и дополнительно атрибут,
    содержащий количество поддерживаемых сим-карт"""
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """Делаем геттер и проверяем на количество сим-карт"""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self._number_of_sim = value


    def __add__(self, other):
        """Складываем объекты Phone и Item"""
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Phone и Item')
        return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
