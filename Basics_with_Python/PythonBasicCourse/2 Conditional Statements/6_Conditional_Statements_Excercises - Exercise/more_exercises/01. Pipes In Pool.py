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
    totPercent = (100 * tot / volume)
    p11 = p1 * 100 / tot
    p22 = p2 * 100 / tot

    print(f"The pool is {totPercent:.2f}% full. Pipe 1: {p11:.2f}%. Pipe 2: {p22:.2f}%.")
else:
    totPercent = (tot - volume)
    print(f"For {time} hours the pool overflows with {totPercent:.2f} liters.")
