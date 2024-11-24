def genrange(start: int, end: int):
    k = start
    while k <= end:
        yield k
        k += 1


print(list(genrange(1, 10)))
