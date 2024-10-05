result_1st = input()
result_2st = input()
result_3rd = input()
wins = 0
loses = 0
draws = 0
a1 = int(result_1st[0])
a2 = int(result_1st[2])
b1 = int(result_2st[0])
b2 = int(result_2st[2])
c1 = int(result_3rd[0])
c2 = int(result_3rd[2])

if a1 > a2:
    wins += 1
elif a1 < a2:
    loses += 1
elif a1 == a2:
    draws += 1

if b1 > b2:
    wins += 1
elif b1 < b2:
    loses += 1
elif b1 == b2:
    draws += 1

if c1 > c2:
    wins += 1
elif c1 < c2:
    loses += 1
elif c1 == c2:
    draws += 1

print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {draws}")
