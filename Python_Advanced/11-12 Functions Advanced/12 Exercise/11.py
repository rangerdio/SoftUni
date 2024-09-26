

def math_operations(*args, **kwargs):
    for i in range(len(args)):
        if i % 4 == 0:
            kwargs["a"] += args[i]
        elif i % 4 == 1:
            kwargs["s"] -= args[i]
        elif i % 4 == 2:
            if args[i] != 0:
                kwargs["d"] /= args[i]
        elif i % 4 == 3:
            kwargs["m"] *= args[i]

    sorting = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    result = ''
    for element, value in sorting:
        result += f'{element}: {value:.1f}\n'
    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))


# from collections import deque
#
#
# def math_operations(*args, **kwargs):
#     args_deque = deque(args)
#
#     counter = 0
#     while args_deque:
#         counter += 1
#         if counter == 5:
#             counter = 1
#         element = args_deque.popleft()
#         if counter == 1:
#             kwargs["a"] += element
#         elif counter == 2:
#             kwargs["s"] -= element
#         elif counter == 3:
#             if element == 0:
#                 continue
#             kwargs["d"] /= element
#         elif counter == 4:
#             kwargs["m"] *= element
#     sorting = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
#     result = ''
#     for element, value in sorting:
#         result += f'{element}: {value:.1f}\n'
#     return result
#
#
# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print(math_operations(6.0, a=0, s=0, d=5, m=0))
