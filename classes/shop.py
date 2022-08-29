from classes.storage import Storage
from exceptions import NotPlaceUniqueItem


class Shop(Storage):

    def __init__(self):
        super().__init__()
        self._capacity = 20

    def add(self, title, count):
        if title not in self.items.keys():
            if self.get_unique_items_count() == 5:
                raise NotPlaceUniqueItem("Нет места для ещё одного товара")

        super().add(title, count)
