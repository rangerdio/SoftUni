import math


def center_point(x1: float, y1: float, x2: float, y2: float):
    c1 = math.sqrt(abs(x1) ** 2 + abs(y1) ** 2)
    c2 = math.sqrt(abs(x2) ** 2 + abs(y2) ** 2)
    if c1 <= c2:
        return f"({math.floor(x1)}, {math.floor(y1)})"
    else:
        return f"({math.floor(x2)}, {math.floor(y2)})"


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
print(center_point(x_1, y_1, x_2, y_2))
