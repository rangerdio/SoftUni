distance = int(input())
rate = input()

bus = 0
taxi = 0
train = 0

if rate == "day":
    taxi = 0.70 + 0.79 * distance
    bus = 0.09 * distance
    train = 0.06 * distance
elif rate == "night":
    taxi = 0.70 + 0.90 * distance
    bus = 0.09 * distance
    train = 0.06 * distance

if distance < 20:
    print(f"{taxi:.2f}")
elif distance >= 20 and distance < 100:
    if taxi < bus:
        print(f"{taxi:.2f}")
    else:
        print(f"{bus:.2f}")
else:
    if taxi <= bus and taxi <= train:
        print(f"{taxi:.2f}")
    elif bus <= taxi and bus <= train:
        print(f"{bus:.2f}")
    else:
        print(f"{train:.2f}")
