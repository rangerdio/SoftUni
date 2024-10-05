points = int(input())
bonus_points = 0

if points <= 100:
    bonus_points = 5
elif points > 100 and points <= 1000:
    bonus_points = points * 0.2
elif points > 1000:
    bonus_points = points * 0.1

if points % 2 == 0:
    bonus_points = bonus_points + 1
elif points % 5 == 0 and  points % 10 != 0:
    bonus_points = bonus_points + 2

print(bonus_points)
print(points + bonus_points)
