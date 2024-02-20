version = list(map(int, input().split(".")))
version[len(version) - 1] += 1
for index in range(-1, -len(version), -1):
    if version[index] == 10:
        version[index] = 0
        version[index - 1] += 1
# result_list = [str(element) for element in version]
# result = ".".join(result_list)
# print(result)
print(".".join([str(element) for element in version]))
