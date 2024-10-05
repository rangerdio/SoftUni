# for _h in range(0,24):
#     for _m in range(0,60):
#         print(f"{_h}:{_m}")

h = -1
m = 0
while h < 23:
    h += 1
    while m < 60:
        print(f"{h}:{m}")
        m += 1
        if m == 60:
            m = 0
            break
