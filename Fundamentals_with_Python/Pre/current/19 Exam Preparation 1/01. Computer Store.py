def taxes(cmd: str, price_total: float):
    if total_price == 0:
        return "Invalid order!"
    if command == "special":
        tax = total_price * 20 / 100
        discount = (tax + total_price) * 0.9
    else:
        tax = total_price * 20 / 100
    return [total_price, tax, total_price + tax]


def calculate_price(price: float):
    if price > 0:   # may be = as well
        price += price
    else:
        print("Invalid price!")
    return price


# tax = 0
total_price = 0
while True:
    command = input()
    if command == "special" or command == "regular":
        result = taxes(command, total_price)
        break
    total_price += calculate_price(float(command))

print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {result[0]:.2f}$")
print(f"Taxes: {result[1]:.2f}$")
print("-----------")
print(f"Total price: {result[2]:.2f}$")
