import os.path
import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []



    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.name}"

    @property
    def name(self):
        """делаем атрибут name приватным"""
        return self.__name


    @name.setter
    def name(self, name_lenght: str):
        """Проверяем что длинна товара не больше 10 символов"""
        if len(name_lenght) > 10:
            raise ValueError("Название товара не должно быть больше 10 символов")
        self.__name = name_lenght


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        cls.all.clear()
        csv_file = os.path.abspath(r"../src/items.csv")
        try:
            with open(csv_file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            print("Нет такого файла")


    @staticmethod
    def string_to_number(string):
        """ статический метод, возвращающий число из числа-строки"""
        try:
            line = float(string)
            return int(line)
        except ValueError:
            print("Ошибка: переданная строка не является числом")
