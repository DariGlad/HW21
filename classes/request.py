from exceptions import ErrorTextRequest


class Request:
    def __init__(self, req: str):
        self._req = req.split()

        try:
            shop_idx = self._req.index("магазин")
            store_idx = self._req.index("склад")

            if store_idx < shop_idx:
                self.from_ = self._req[store_idx]
                self.to = self._req[shop_idx]

            if shop_idx < store_idx:
                self.from_ = self._req[shop_idx]
                self.to = self._req[store_idx]

            self.product = self._req[self._req.index("из") - 1]
            amount = self._req[self._req.index(self.product) - 1]
            if not amount.isdigit():
                self.amount = None

            self.amount = int(amount)

        except(ValueError, IndexError):
            raise ErrorTextRequest("Неверный формат запроса\n"
                                   "Пример: 'Доставить 3 печеньки из склад в магазин'")
