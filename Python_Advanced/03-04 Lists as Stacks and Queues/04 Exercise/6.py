# from collections import deque
#
# is_unbalanced = False
# opening_deque = deque()
# opening = "([{"
# closing = ")]}"
# parentheses = deque(input())
#
# while parentheses:
#     element = parentheses.popleft()
#     if element in opening:
#         opening_deque.append(element)
#     elif element in closing:
#         index = closing.index(element)
#         if opening_deque and opening_deque[len(opening_deque) - 1] == opening[index]:
#             opening_deque.pop()
#         else:
#             is_unbalanced = True
#             break
#
# if len(opening_deque) != 0:
#     is_unbalanced = True
#
# print("YES") if not is_unbalanced else print("NO")


is_unbalanced = False
stack = []
opening = "([{"
closing = ")]}"
parentheses = input()

for element in parentheses:
    if element in opening:
        stack.append(element)
    elif element in closing:
        index = closing.index(element)
        if stack and stack[len(stack) - 1] == opening[index]:
            stack.pop()
        else:
            is_unbalanced = True
            break

if len(stack) != 0:
    is_unbalanced = True

print("YES") if not is_unbalanced else print("NO")


# from collections import deque
#
# parentheses = deque(input())
# opening = "([{"
# closing = ")]}"
# counter = 0
#
# while parentheses and counter < len(parentheses) / 2:
#     if parentheses[0] in closing:
#         break
#     else:
#         index = opening.index(parentheses[0])
#
#         if parentheses[1] == closing[index]:
#             parentheses.popleft()
#             parentheses.popleft()
#             parentheses.rotate(counter)
#             counter = 0
#         else:
#             parentheses.rotate(-1)
#             counter += 1
# print("NO") if parentheses else print("YES")





#
# from collections import deque
# is_balanced = True
#
# parentheses_deque = deque(input().strip())
#
# if len(parentheses_deque) % 2 == 1:
#     is_balanced = False
#
# matching_pairs = {")": "(", "]": "[", "}": "{", "(": ")", "[": "]", "{": "}"}
#
# while parentheses_deque and is_balanced:
#
#     left = parentheses_deque.popleft()
#     right = parentheses_deque.pop()
#
#     if left != matching_pairs[right]:
#         is_balanced = False
#         break
#
# print("YES") if is_balanced else print("NO")
