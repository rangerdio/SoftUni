# for _i in range (1, 11):
#     for _n in range (1, 11):
#         print(f"{_i} * {_n} = {_i * _n}")
i = 1
n = 1
while i < 11:
    while n < 11:
        print(f"{i} * {n} = {i * n}")
        n += 1
    else:
        n = 1
    i += 1