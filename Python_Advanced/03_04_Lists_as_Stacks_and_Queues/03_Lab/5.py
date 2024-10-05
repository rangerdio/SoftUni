from collections import deque

kids = deque(input().split())
n = int(input()) - 1

while len(kids) > 1:
    kids.rotate(-n)
    print(f"Removed {kids.popleft()}")
print(f"Last is {kids.pop()}")

# from collections import deque
#
# kids = deque(input().split())
# n = int(input()) - 1
#
# while len(kids) > 1:
#     for i in range(n):
#         current_kid = kids.popleft()
#         kids.append(current_kid)
#     print(f"Removed {kids.popleft()}")
# print(f"Last is {kids.pop()}")
