from classes.storage import Storage


class Store(Storage):
    def __init__(self):
        super().__init__()
        self._capacity = 100
