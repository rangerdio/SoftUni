from math import floor
tournaments = int(input())
start_points = int(input())
points = start_points
winner = 0
for number in range(1, tournaments + 1):
    result = input()
    if result == "W":
        points += 2000
        winner += 1
    elif result == "F":
        points += 1200
    elif result == "SF":
        points += 720
average = floor((points - start_points) / tournaments)
win = winner / tournaments * 100
print(f"Final points: {points}")
print(f"Average points: {average}")
print(f"{win:.2f}%")
