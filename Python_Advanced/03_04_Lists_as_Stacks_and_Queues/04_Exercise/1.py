# numbers = input().split()
# rev = []
# while numbers:
#     rev.append(numbers.pop())
# print(" ".join(rev))

from collections import deque
numbers = deque(input().split())

for _ in range(len(numbers)):
    print(numbers.pop(), end=" ")
