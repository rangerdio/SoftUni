import math

number = int(input())
points = 0
red_cnt = 0
orange_cnt = 0
yellow_cnt = 0
white_cnt = 0
others_cnt = 0
black_cnt = 0

for i in range(number):
    ball = input()

    if ball == "red":
        red_cnt += 1
        points += 5
    elif ball == "orange":
        orange_cnt += 1
        points += 10
    elif ball == "yellow":
        yellow_cnt += 1
        points += 15
    elif ball == "white":
        white_cnt += 1
        points += 20
    elif ball == "black":
        black_cnt += 1
        points = math.floor(points / 2)
    else:
        others_cnt += 1

print(f"Total points: {points}")
print(f"Red balls: {red_cnt}")
print(f"Orange balls: {orange_cnt}")
print(f"Yellow balls: {yellow_cnt}")
print(f"White balls: {white_cnt}")
print(f"Other colors picked: {others_cnt}")
print(f"Divides from black balls: {black_cnt}")
