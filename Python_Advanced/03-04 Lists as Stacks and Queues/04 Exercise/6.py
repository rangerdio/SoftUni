from collections import deque
is_balanced = True

parentheses_string = input()
if len(parentheses_string) % 2 == 1:
    is_balanced = False

parentheses_deque = deque(parentheses_string)


while len(parentheses_deque) > 0:
    left = parentheses_deque.popleft()
    right = parentheses_deque.pop()

    if left == "(":
        if right == ")":
            continue
        else:
            is_balanced = False
            break
    elif left == "{":
        if right == "}":
            continue
        else:
            is_balanced = False
            break
    elif left == "[":
        if right == "]":
            continue
        else:
            is_balanced = False
            break

print("YES") if is_balanced else print("NO")
