from collections import deque
q = deque(x for x in input().split())
box_result = 0
varr = 0
box = deque()
operators = ['+', '-', '*', '/']

while q:
    current = q.popleft()
    if current.isdigit() or len(current) > 1:
        box.append(current)

    else:
        if current == '-':
            if box_result == 0:
                varr += float(box.popleft())
            else:
                varr = box_result
            while box:
                varr -= float(box.popleft())
            box_result = varr
            varr = 0
            # print(box_result)

        elif current == '*':
            # if box_result == 0:
            #     box_result += 1
            varr = box_result * 1
            while box:
                sss = box.popleft()
                varr *= float(sss)

            box_result = varr
            varr = 0
            # print(box_result)

        elif current == '/':
            varr = box_result * 1
            while box:
                varr //= float(box.popleft())
            box_result = varr
            varr = 0
            # print(box_result)

        elif current == '+':
            varr = box_result
            while box:
                varr += float(box.popleft())
            box_result = varr
            varr = 0
            # print(box_result)

print(int(box_result))
