rest_days = int(input())
max_playtime = 30000
work_days = 365 - rest_days
workday_playtime = 63 * work_days
restday_playtime = 127 * rest_days
total_playtime = workday_playtime + restday_playtime
if total_playtime > max_playtime:
    print(f"Tom will run away")
    print(f"{(total_playtime - max_playtime) // 60} hours and {(total_playtime - max_playtime) % 60} minutes more for play")
else:
    print(f"Tom sleeps well")
    print(f"{(max_playtime - total_playtime) // 60} hours and {(max_playtime - total_playtime) % 60} minutes less for play")
    