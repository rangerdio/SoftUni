first = int(input())
second = int(input())
third = int(input())
sbor = first + second + third

min = sbor // 60
sec = sbor % 60

if sec < 10:
    print(f"{min}:0{sec}")
else:
    print(f"{min}:{sec}")