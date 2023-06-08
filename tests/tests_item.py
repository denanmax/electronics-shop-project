"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item, InstantiateCSVError
from src.phone import Phone
from src.keyboard import KeyBoard
import pytest
import pathlib
from pathlib import Path
dir_path = pathlib.Path.cwd()


def test_init():
    """Тесты проверки функции init"""
    item = Item("Микрофон", 2000, 3)
    assert item.name == "Микрофон"
    assert item.price == 2000
    assert item.quantity == 3
    # проверка при нулево стоке
    item = Item("Дискошар", 10.0, 0)
    assert item.calculate_total_price() == 0
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'



def test_calculate_total_price():
    """Вывод общей суммы по количеству"""
    assert Item("Микрофон", 1000, 5).calculate_total_price() == 5000


def test_apply_discount():
    """Вывод общей суммы при скидке"""
    item = Item("Микрофон", 2000, 3)
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 1600


def test_name():
    item = Item('Телефон', 10000, 5)
    item.name = "Смартфон"
    assert item.name == "Смартфон"


def test_name_setter():
    with pytest.raises(ValueError):
        Item('Квадракоптер', 10000, 5)
    item = Item('Дрон', 5000, 8)
    assert item.name == 'Дрон'


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    Item.instantiate_from_csv()
    assert Item.instantiate_from_csv() is None
    with pytest.raises(TypeError):
        Item.instantiate_from_csv("/src/item.py")



def test_repr():
    with pytest.raises(TypeError):
        repr(Item(12, 10000, 20))
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    item2 = Item("Смартфон", -200, -500)
    assert repr(item2) == "Item('Смартфон', -200, -500)"
    item3 = Item('Телек', "2200", "500")
    assert repr(item3) == "Item('Телек', 2200, 500)"

def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    phone1 = 50000
    with pytest.raises(AttributeError):
        item1.__add__(phone1)
    phone = Phone("iPhone", "Apple", 1000, 2)
    other = "Some object"
    with pytest.raises(ValueError):
        phone.__add__(other)
    phone2 = Phone("Galaxy", "Samsung", 800, 1)
    assert phone + phone2 == 1800

def tests_phone():
    phone = Phone("iPhone", 1000, 10, 2)
    assert phone.name == "iPhone"
    assert phone.price == 1000
    assert phone.quantity == 10
    assert phone.number_of_sim == 2
    item = Item("Case", 10, 5)
    assert phone.__add__(item) == 15

def test_nums_of_sim():
    phone = Phone("iPhone", 1000, 10, 2)
    with pytest.raises(ValueError):
        Phone("iPhone", 1000, 10, -1)
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1
    with pytest.raises(ValueError):
        phone.number_of_sim = -1

def test_phone_repr():
    phone = Phone("iPhone", 1000, 10, 2)
    assert repr(phone) == "Phone('iPhone', 1000, 10, 2)"

def test_keyboard():
    kb = KeyBoard('Defender LUX', 9600, 5)
    assert str(kb) == "Defender LUX"
    assert kb.price == 9600
    assert kb.rating == 5

def test_keyboard_lang():
    kb = KeyBoard('Defender LUX', 9600, 5)
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
    with pytest.raises(AttributeError):
        kb.language = 'CH'

def test_FileNotFoundError_errors():
    file = ''
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(file)

def test_InstantiateCSVError_errors():
    path_incorrect_file = Path(dir_path, '../src/test_item.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(path_incorrect_file)