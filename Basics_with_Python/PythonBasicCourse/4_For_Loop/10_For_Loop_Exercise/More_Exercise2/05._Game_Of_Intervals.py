result = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
game_steps = int(input())
for _num in range(1, game_steps + 1):
    number = int(input())
    if 0 <= number <= 9:
        result += 0.20 * number
        a += 1
    elif 10 <= number <= 19:
        result += 0.30 * number
        b += 1
    elif 20 <= number <= 29:
        result += 0.40 * number
        c += 1
    elif 30 <= number <= 39:
        result += 50
        d += 1
    elif 40 <= number <= 50:
        result += 100
        e += 1
    elif number < 0 or number > 50:
        result /= 2
        f += 1
print(f"{result:.2f}")
print(f"From 0 to 9: {(100 * a / game_steps ):.2f}%")
print(f"From 10 to 19: {(100 * b / game_steps ):.2f}%")
print(f"From 20 to 29: {(100 * c / game_steps ):.2f}%")
print(f"From 30 to 39: {(100 * d / game_steps ):.2f}%")
print(f"From 40 to 50: {(100 * e / game_steps ):.2f}%")
print(f"Invalid numbers: {(100 * f / game_steps ):.2f}%")
