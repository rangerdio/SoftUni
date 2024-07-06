# from collections import deque
# is_balanced = True
#
# parentheses_deque = deque(input())
#
# if len(parentheses_deque) % 2 == 1:
#     is_balanced = False
#
# while parentheses_deque:
#     if not is_balanced:
#         break
#     left = parentheses_deque.popleft()
#     right = parentheses_deque.pop()
#
#     if left == "(":
#         if right == ")":
#             continue
#         else:
#             is_balanced = False
#             break
#     elif left == "{":
#         if right == "}":
#             continue
#         else:
#             is_balanced = False
#             break
#     elif left == "[":
#         if right == "]":
#             continue
#         else:
#             is_balanced = False
#             break
#
# print("YES") if is_balanced else print("NO")


from collections import deque
is_balanced = True

parentheses_deque = deque(input().strip())

if len(parentheses_deque) % 2 == 1:
    is_balanced = False

matching_pairs = {")": "(", "]": "[", "}": "{", "(": ")", "[": "]", "{": "}"}

while parentheses_deque and is_balanced:

    left = parentheses_deque.popleft()
    right = parentheses_deque.pop()

    if left != matching_pairs[right]:
        is_balanced = False
        break

print("YES") if is_balanced else print("NO")
