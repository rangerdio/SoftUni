budged = float(input())
nights = int(input())
night_price = float(input())
adds_percent = int(input())

if nights > 7:
    night_price = 0.95 * night_price

total = nights * night_price
adds = adds_percent * budged / 100
grand_total = total + adds
if grand_total <= budged:
    print(f"Ivanovi will be left with {(abs(grand_total - budged)):.2f} leva after vacation.")
else:
    print(f"{(abs(budged - grand_total)):.2f} leva needed.")