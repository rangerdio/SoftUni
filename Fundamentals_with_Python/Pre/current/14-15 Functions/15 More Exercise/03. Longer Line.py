import math


def point_1_closer(x1, y1, x2, y2):
    c1 = math.sqrt(abs(x1) ** 2 + abs(y1) ** 2)
    c2 = math.sqrt(abs(x2) ** 2 + abs(y2) ** 2)
    if c1 <= c2:
        # print("True")
        return True
    else:
        # print("False")
        return False


def longer_line(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float):
    line_1 = math.sqrt((abs(x1) + abs(x2)) ** 2 + (abs(y1) - abs(y2)) ** 2)
    line_2 = math.sqrt((abs(x3) + abs(x4)) ** 2 + (abs(y3) + abs(y4)) ** 2)
    if line_1 >= line_2:
        # print("line_1 winner")
        winner_line_x1 = x1
        winner_line_y1 = y1
        winner_line_x2 = x2
        winner_line_y2 = y2
        if point_1_closer(winner_line_x1, winner_line_y1, winner_line_x2, winner_line_y2):
            return (
                f"({math.floor(winner_line_x1)}, {math.floor(winner_line_y1)})"
                f"({math.floor(winner_line_x2)}, {math.floor(winner_line_y2)})"
            )
        else:
            return (
                f"({math.floor(winner_line_x2)}, {math.floor(winner_line_y2)})"
                f"({math.floor(winner_line_x1)}, {math.floor(winner_line_y1)})"
            )
    else:
        # print("line_2 winner")
        winner_line_x1 = x3
        winner_line_y1 = y3
        winner_line_x2 = x4
        winner_line_y2 = y4
        if point_1_closer(winner_line_x1, winner_line_y1, winner_line_x2, winner_line_y2):
            return (
                f"({math.floor(winner_line_x1)}, {math.floor(winner_line_y1)})"
                f"({math.floor(winner_line_x2)}, {math.floor(winner_line_y2)})"
            )
        else:
            return (
                f"({math.floor(winner_line_x2)}, {math.floor(winner_line_y2)})"
                f"({math.floor(winner_line_x1)}, {math.floor(winner_line_y1)})"
            )


# x_1 = 1
# y_1 = 2
# x_2 = 3
# y_2 = 4
# x_3 = 9
# y_3 = 7
# x_4 = 5
# y_4 = 6
x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())
print(longer_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4))
