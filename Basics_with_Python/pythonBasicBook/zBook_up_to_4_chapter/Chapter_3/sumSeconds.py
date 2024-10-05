user1 = int(input())
user2 = int(input())
user3 = int(input())
secondsTotal = user3 + user2 + user1
min = 0
sec = 0
if secondsTotal < 60:
    min = 0
    sec = secondsTotal
if secondsTotal >= 60 and secondsTotal < 120:
    min = 1
    sec = secondsTotal - 60
if secondsTotal >= 120:
    min = 2
    sec = secondsTotal - 120
if sec < 10:
    print(f"{min}:0{sec}")
else:
    print(f"{min}:{sec}")
