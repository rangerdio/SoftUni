from collections import deque
q = deque(x for x in input().split())
result = 0
varr = 0
box = deque()
flag = False  # validate how we proceed operations when result is "0" (initial "0" or "0" after first found operator)
operators = ['+', '-', '*', '/']
while q:

    curr_item = q.popleft()
    if curr_item.isdigit() or len(curr_item) > 1:
        box.append(int(curr_item))

    elif curr_item == '*':
        varr = result
        if varr == 0 and not flag:  # if "0" as initial, then just add item from box without any operations
            varr = int(box.popleft())

            while box:
                varr *= box.popleft()

        else:
            while box:
                varr *= box.popleft()
        result = varr
        flag = False

    elif curr_item == '-':
        varr = result
        if varr == 0 and not flag:  # if "0" as initial, then just add item from box without any operations
            varr = box.popleft()

            while box:
                varr -= int(box.popleft())

        else:
            while box:
                varr -= box.popleft()
        result = varr
        flag = False

    elif curr_item == '+':
        varr = result
        while box:
            varr += box.popleft()
        result = varr

    elif curr_item == '/':
        flag = False
        varr = result
        if varr == 0 and not flag:  # if "0" as initial, then just add item from box without any operations
            varr = int(box.popleft())

            while box:
                varr //= box.popleft()

        else:
            while box:
                varr //= box.popleft()
        result = varr
        flag = False

print(result)
