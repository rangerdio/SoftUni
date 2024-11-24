def squares(n):
    m = 1
    while m <= n:
        yield m * m
        m += 1


print(list(squares(5)))
