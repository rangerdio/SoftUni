# stack = []
# n = int(input())
#
# for _ in range(n):
#     query = input().split()
#     if query[0] == "2":
#         if stack:
#             stack.pop()
#     elif query[0] == "3":
#         if stack:
#             print(max(stack))
#     elif query[0] == "4":
#         if stack:
#             print(min(stack))
#     else:
#         stack.append(int((query[1])))
#
# stack.reverse()
# print(*stack, sep=", ")

stack = []
map_functions = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop(x[1]) if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}

for _ in range(int(input())):
    data = input().split()
    command = data[0]

n = int(input())

for _ in range(n):
    query = input().split()
    if query[0] == "2":
        if stack:
            stack.pop()
    elif query[0] == "3":
        if stack:
            print(max(stack))
    elif query[0] == "4":
        if stack:
            print(min(stack))
    else:
        stack.append(int((query[1])))

stack.reverse()
print(*stack, sep=", ")
