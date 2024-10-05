import re
string = input()
pattern = r"[ ]?\+359[ ]2[ ]\d{3}[ ]\d{4}\b|[ ]?\+359[-]2[-]\d{3}[-]\d{4}\b"
result = re.findall(pattern, string)

for i in range(len(result)):
    if i != len(result) - 1:
        print(result[i].lstrip() + ",", end=" ")
    else:
        print(result[i].lstrip())
