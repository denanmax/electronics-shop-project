"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


def test_init():
    """Тесты проверки функции init"""
    item = Item("Видеомагнитофон", 2000, 3)
    assert item.name == "Видеомагнитофон"
    assert item.price == 2000
    assert item.quantity == 3
    # проверка при нулево стоке
    item = Item("Дискошар", 10.0, 0)
    assert item.calculate_total_price() == 0
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'



def test_calculate_total_price():
    """Вывод общей суммы по количеству"""
    assert Item("Автомагнитола", 1000, 5).calculate_total_price() == 5000


def test_apply_discount():
    """Вывод общей суммы при скидке"""
    item = Item("DVD проигрыватель", 2000, 3)
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 1600


def test_name():
    item = Item('Телефон', 10000, 5)
    item.name = "Смартфон"
    assert item.name == "Смартфон"

def test_name_setter():
    item = Item('Квадракоптер', 10000, 5)
    with pytest.raises(ValueError):
        item.name = "Название товара не должно быть больше 10 символов"
