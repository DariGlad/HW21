from classes.base_storage import BaseStorage
from exceptions import NotPlaceForItems, NotFoundItems, NotEnoughItems, ErrorCount


class Storage(BaseStorage):
    def __init__(self):
        self._items = {}
        self._capacity = 0

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, title, count):
        if count <= self.get_free_space():
            self.items[title] = self.items.get(title, 0) + count
        else:
            raise NotPlaceForItems("Нет свободных мест")

    def remove(self, title, count):
        if self.items.get(title) is None:
            raise NotFoundItems("Товар не найден")

        if count < 0:
            raise ErrorCount("Количество не должно иметь отрицательное значение")

        if self.items.get(title) >= count:
            self.items[title] = self.items.get(title) - count

        else:
            raise NotEnoughItems("Нет нужного количества товаров")

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(set(self.items.keys()))
