start_str = input()
end_str = input()
skip_str = input()
counter = 0
start_num = ord(start_str)
end_num = ord(end_str)
skip_num = ord(skip_str)

for first in range(start_num, end_num + 1):
    if first == skip_num:
        continue
    for second in range(start_num, end_num + 1):
        if second == skip_num:
            continue
        for third in range(start_num, end_num + 1):
            if third == skip_num:
                continue
            print(chr(first)+chr(second)+chr(third), end=" ")
            counter += 1
print(counter)
