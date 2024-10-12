from collections import deque


def shop_from_grocery_list(budged, grocery_list, *products):
    products_list = deque(products)
    bought_products = []

    for _ in range(len(products)):
        product, price = products_list.popleft()
        if budged < price:
            break
        else:
            if product in grocery_list:
                if product in bought_products:
                    continue
                budged -= price
                grocery_list.remove(product)
    if not grocery_list:
        return f'Shopping is successful. Remaining budget: {budged:.2f}.'
    else:
        return f'You did not buy all the products. Missing products: {", ".join(grocery_list)}.'


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
