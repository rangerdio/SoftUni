from math import sqrt


def center_point(x1: float, y1: float, x2: float, y2: float):
    c1 = sqrt(abs(x1) ** 2 + abs(y1) ** 2)
    c2 = sqrt(abs(x2) ** 2 + abs(y2) ** 2)
    if c1 <= c2:
        return f"({int(x1)}, {int(y1)})"
    else:
        return f"({int(x2)}, {int(y2)})"


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
print(center_point(x_1, y_1, x_2, y_2))
