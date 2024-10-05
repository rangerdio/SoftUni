nonWorkDays = int(input())

workDays = 365 - nonWorkDays
playTimeRest = nonWorkDays * 127
playTimeWork = workDays * 63
playTime = playTimeWork + playTimeRest
norm = 30000

if playTime > norm:
    print("Tom will run away")
    print(f"{(playTime - norm) // 60} hours and {(playTime - norm) % 60} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{(norm - playTime) // 60} hours and {(norm - playTime) % 60} minutes less for play")