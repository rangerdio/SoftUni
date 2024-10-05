distance = int(input("Enter lenght: "))
time = input("day or night? ")

taxi = 0
bus = 0
train = 0
if distance < 20:
    if time == "day":
        taxi = 0.7 + 0.79 * distance
        print(taxi)
    elif time == "night":
        taxi = 0.7 + 0.9 * distance
        print(taxi)
elif distance >= 20 and distance < 100:
    if time == "day":
        taxi = 0.7 + 0.79 * distance
        bus = 0.09 * distance
        if taxi < bus and taxi != 0:
            print(taxi)
        else: print(bus)

    elif time == "night":
        taxi = 0.7 + 0.9 * distance
        bus  = 0.09 * distance
        if taxi < bus and taxi != 0:
            print(taxi)
        else: print(bus)
elif distance >= 100:
    if time == "day":
        taxi = 0.7 + 0.79 * distance
        bus  = 0.09 * distance
        train = 0.06 * distance
        a = taxi,bus,train
        print(min(a))
    if time == "night":
        taxi = 0.7 + 0.9 * distance
        bus  = 0.09 * distance
        train = 0.06 * distance
        a = taxi,bus,train
        print(min(a))