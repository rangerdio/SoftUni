x = float(input())
y = float(input())
h = float(input())

sides = (x * x - 2 * 1.2) + x * x + 2 * (x * y - 1.5 * 1.5)
roof = 2 * x * y + x * h
green = sides / 3.4
red = roof / 4.3

print(f"{green:.2f}")
print(f"{red:.2f}")