"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src import item
from src.item import Item


def test_init():
    """Тесты проверки функции init"""
    item = Item("Видеомагнитофон", 2000, 3)
    assert item.name == "Видеомагнитофон"
    assert item.price == 2000
    assert item.quantity == 3
    # проверка при нулево стоке
    item = Item("Дискошар", 10.0, 0)
    assert item.calculate_total_price() == 0


def test_calculate_total_price():
    """Вывод общей суммы по количеству"""
    assert Item("Автомагнитола", 1000, 5).calculate_total_price() == 5000

def test_apply_discount():
    """Вывод общей суммы при скидке"""
    item = Item("DVD проигрыватель", 2000, 3)
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 1600