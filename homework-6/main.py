import pathlib

from src.item import Item
from pathlib import Path

dir_path = pathlib.Path.cwd()


if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    path_incorrect_file = Path(dir_path, '../src/test_item.csv')
    Item.instantiate_from_csv(path_incorrect_file)
    # InstantiateCSVError: Файл item.csv поврежден