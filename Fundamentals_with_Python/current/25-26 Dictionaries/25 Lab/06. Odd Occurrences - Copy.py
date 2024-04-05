words = input().lower().split()
dictionary = {}
for word in words:
    if word not in dictionary.keys():
        dictionary[word] = 1
    else:
        dictionary[word] += 1
for word, count in dictionary.items():
    if count % 2 == 1:
        print(word, end=" ")
