class MixinLanguage:
    """Mixin для хранения и изменения аскладки клавиатуры"""
    def __init__(self):
        self._language = 'EN'

    def change_lang(self):
        self._language = 'RU' if self._language == 'EN' else 'EN'
        return self


class KeyBoard(MixinLanguage):
    """Класс для товара клавиатура"""
    def __init__(self, name, price, rating):
        super().__init__()
        self.name = name
        self.price = price
        self.rating = rating

    def __str__(self):
        return self.name

    @property
    def language(self):
        return self._language
