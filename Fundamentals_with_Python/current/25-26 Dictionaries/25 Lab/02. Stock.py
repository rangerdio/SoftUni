products_list = input().split()
products = {}
search_list = input().split()

for i in range(0, len(products_list), 2):
    products[products_list[i]] = int(products_list[i+1])

for product in search_list:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
