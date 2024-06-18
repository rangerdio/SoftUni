dictionary = {}
n = int(input())
for i in range(n):
    word = input()
    synonym = input()
    if word not in dictionary.keys():
        dictionary[word] = [synonym]
    else:
        dictionary[word].append(synonym)

for key in dictionary.keys():
    print(f"{key} - {', '.join(dictionary[key])}")
