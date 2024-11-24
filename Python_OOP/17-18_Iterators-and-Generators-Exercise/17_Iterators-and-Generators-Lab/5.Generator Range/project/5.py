def genrange(start: int, end: int):
    for k in range(start, end +1):
        yield k


print(list(genrange(1, 10)))
