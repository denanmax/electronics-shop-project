import os.path
import sys
import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV = '/home/denis/PycharmProjects/electronics-shop-project/src/items.csv'


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_lenght: str):
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
        cls.all.clear()
        try:
            with open(cls.CSV, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            print("Нет такого файла")

    @staticmethod
    def string_to_number(string):
        try:
            line = float(string)
            return int(line)
        except ValueError:
            print("Ошибка: переданная строка не является числом")
