ver = "3.9.9"
version = ver.split(".")
print(version[2])
#version[int(len(version) - 1)] += 1
for index in range(-1, -len(version), -1):
    if version[index] == 10:
        version[index] = 0
        version[index - 1] += 1
#print(version)
