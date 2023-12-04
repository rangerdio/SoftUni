# counter = 0
# n = int(input())
# for a in range(n + 1):
#     for b in range(n + 1):
#         for c in range(n + 1):
#             if (a + b + c) == n:
#                 counter += 1
# print(counter)

counter = 0
a = 0
b = 0
c = 0
n = int(input())
while a <= n:
    while b <= n:
        while c <= n:
            if (a + b + c ) == n:
                counter += 1
            c += 1
        else:
            c = 0
        b +=1
    else:
        b = 0
    a += 1
print(counter)
