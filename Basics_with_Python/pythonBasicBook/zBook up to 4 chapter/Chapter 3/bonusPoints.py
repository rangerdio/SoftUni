points = int(input())
bonus = 0
bonus2=0
if points % 2 == 0:
    bonus2 = 1
elif points % 5 == 0 and points % 10 != 0:
    bonus2 = 2

if points <= 100:
    bonus = 5
elif points > 100 and points <= 1000:
    bonus = points * 0.2
elif points > 1000:
    bonus = points * 0.1

print(f"{bonus+bonus2}")
print(f"{points+bonus+bonus2}")
