from collections import deque

parentheses = deque(input())
opening = "([{"
closing = ")]}"
counter = 0

while parentheses and counter < len(parentheses) / 2:
    if parentheses[0] in closing:
        break
    else:
        index = opening.index(parentheses[0])

        if parentheses[1] == closing[index]:
            parentheses.popleft()
            parentheses.popleft()
            parentheses.rotate(counter)
            counter = 0
        else:
            parentheses.rotate(-1)
            counter += 1
print("NO") if parentheses else print("YES")

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
