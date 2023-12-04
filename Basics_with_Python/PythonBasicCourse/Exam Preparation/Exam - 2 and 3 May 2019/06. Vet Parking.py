days = int(input())
hours_during_day = int(input())
total = 0
total_day = 0

for day in range(1, days + 1):
    total_day = 0
    for hour in range(1, hours_during_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            total_day += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            total_day += 1.25
        else:
            total_day += 1
    print(f"Day: {day} - {total_day:.2f} leva")
    total += total_day
print(f"Total: {total:.2f} leva")
