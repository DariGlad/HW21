from classes.request import Request
from classes.shop import Shop
from classes.store import Store
from constants import START_TEXT, ACTIONS_TEXT
from exceptions import ErrorTextRequest, NotPlaceForItems, NotFoundItems, NotEnoughItems, NotPlaceUniqueItem, ErrorCount

input(START_TEXT)

store = Store()
store.add("печеньки", 1)
store.add("конфеты", 10)
store.add("шоколад", 15)
store.add("мармелад", 5)
store.add("сгущенка", 15)
store.add("пепси", 15)

shop = Shop()
shop.add("конфеты", 1)
shop.add("пепси", 2)
shop.add("шоколад", 3)
shop.add("мармелад", 2)
shop.add("сгущенка", 4)

while True:
    user_input = input(">>>").lower().strip()
    if user_input in ("exit", "выход"):
        print("Пока")
        quit()

    try:
        request = Request(user_input)
    except ErrorTextRequest as e:
        print(e)
        continue

    try:
        if request.from_ == "склад":
            store.remove(request.product, request.amount)
            shop.add(request.product, request.amount)

        if request.from_ == "магазин":
            shop.remove(request.product, request.amount)
            store.add(request.product, request.amount)
    except (NotPlaceForItems,
            NotFoundItems,
            NotEnoughItems,
            NotPlaceUniqueItem,
            ErrorCount) as e:
        print(e)
        continue

    print(ACTIONS_TEXT.format(
        from_=request.from_,
        to=request.to,
        amount=request.amount,
        product=request.product
    ))
    print("На складе хранится:")

    store_items = store.get_items()
    for title, count in store_items.items():
        print(count, title)

    print("В магазине хранится:")

    shop_items = shop.get_items()
    for title, count in shop_items.items():
        print(count, title)
