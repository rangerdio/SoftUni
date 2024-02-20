budged = float(input())
flour_price_kg = float(input())
loaves_cnt = 0
colored_eggs_cnt = 0
cnt = 0

egg_pack_price = 0.75 * flour_price_kg
milk_recipe_price = (1.25 * flour_price_kg) / 4

loaves_products_price = flour_price_kg + egg_pack_price + milk_recipe_price

while budged >= loaves_products_price:
    budged -= loaves_products_price
    colored_eggs_cnt += 3
    loaves_cnt += 1
    if loaves_cnt % 3 == 0:
        colored_eggs_cnt = colored_eggs_cnt - (loaves_cnt - 2)

print(f"You made {loaves_cnt} loaves of Easter bread! Now you have {colored_eggs_cnt} eggs and {budged:.2f}BGN left.")
