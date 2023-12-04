n = int(input())
k = int(input())
magic = int(input())
counter = 0
found = False

for _n in range(n, k + 1):
    for _k in range(n, k + 1):
        counter += 1
        if _n + _k == magic:
            print(f"Combination N:{counter} ({_n} + {_k} = {_n + _k})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{counter} combinations - neither equals {magic}")

# n = int(input())
# k = int(input())
# n1 = n
# n2 = n
#
# magic = int(input())
# counter = 0
# found = False
#
# while n1 <= k:
#     while n2 <= k:
#         counter += 1
#         if n1 + n2 == magic:
#             found = True
#             print(f"Combination N:{counter} ({n1} + {n2} = {n1 + n2})")
#             break
#         n2 += 1
#     if found:
#         break
#     n2 = n
#     n1 += 1
# if not found:
#     print(f"{counter} combinations - neither equals {magic}")
#             break
#         __n += 1
#     if found:
#         break
#     __n = n
#     _n += 1
# if not found:
#     print(f"{counter} combinations - neither equals {magic}")
