fig = input()
if fig == "square":
    a = float(input())
    area = a * a
    print(round(area,3))
elif fig == "rectangle":
    a = float(input())
    b = float(input())
    print(round(a * b,3))
elif fig == "circle":
    r = float(input())
    import math
    print(round(math.pi * r * r,3))
elif fig == "triangle":
    a = float(input())
    ha = float(input())
    print(round(a * ha / 2,3))
else:
    print("Unrecognized figure!")