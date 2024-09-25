def koko(num):
    if num == 998:
        return num
    return koko(num + 1)
print(koko(1))
