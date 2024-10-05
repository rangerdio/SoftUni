import math
volume = int(input())
p1 = int(input())
p2 = int(input())
time = float(input())

p1 = p1 * time
p2 = p2 * time
tot = p1 + p2
totPercent = 0

if volume >= tot:
    totPercent = math.trunc(100 * tot / volume)
    p1 = math.trunc(p1 * 100 / tot)
    p2 = math.trunc(p2 * 100 / tot)

    print(f"The pool is {totPercent}% full. Pipe 1: {p1}%. Pipe 2: {p2}%.")
else:
    totPercent = (tot - volume)
    print(f"For {time} hours the pool overflows with {totPercent} liters.")
