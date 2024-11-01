n = int(input())


def combine(nn):
    return upper_side(nn) + lower_side(nn)


def upper_side(size):
    result = ''
    for i in range(size + 1):
        stars = i
        spaces = n - i
        # if i == size:
        #     result += f"{' ' * spaces}{'* ' * stars}"
        # else:
        #     result += f"{' ' * spaces}{'* ' * stars}\n"3
        result += f"{' ' * spaces}{'* ' * stars}\n"
    return result


def lower_side(size):
    result = ''
    for i in range(size - 1):
        stars = size - 1 - i
        spaces = i + 1
        result += f"{' ' * spaces}{'* ' * stars}\n"
    return result


print(combine(n))
