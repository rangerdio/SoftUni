def orders(order: str, quantity: int):
    price = 0
    if order == "coffee":
        price = 1.50
    elif order == "water":
        price = 1.00
    elif order == "coke":
        price = 1.40
    elif order == "snacks":
        price = 2.00
    return price * quantity


print(f"{orders(input(), int(input())):.2f}")
