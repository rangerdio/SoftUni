line_lst = input().split()
line_result = ""
for word in line_lst:
    line_result += word * len(word)
print(line_result)
