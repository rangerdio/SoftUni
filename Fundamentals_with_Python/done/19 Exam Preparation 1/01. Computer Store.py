def taxes(cmd: str, price_total: float):

    if cmd == "special":
        tax = price_total * 20 / 100
        taxed = total_price + tax
        discount = taxed * 0.1
    else:
        tax = price_total * 20 / 100
        taxed = total_price + tax
        discount = 0

    after_tax_and_discount = taxed - discount
    return [price_total, tax, after_tax_and_discount]


total_price = 0
while True:
    command = input()
    if command == "special" or command == "regular":
        result = taxes(command, total_price) if total_price != 0 else print("Invalid order!")
        break
    current_price = float(command)
    if current_price > 0:
        total_price += current_price
    else:
        print("Invalid price!")

if result:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {result[0]:.2f}$")
    print(f"Taxes: {result[1]:.2f}$")
    print("-----------")
    print(f"Total price: {result[2]:.2f}$")
