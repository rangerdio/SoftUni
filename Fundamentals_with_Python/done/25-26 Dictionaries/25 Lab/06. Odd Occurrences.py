element_list = input().split()
elements = {}
elements_list_lowered = []
[elements_list_lowered.append(word.lower()) for word in element_list]

for word in elements_list_lowered:
    if word not in elements.keys():
        elements[word] = 0
    else:
        elements[word] += 1

for word, value in elements.items():
    if value % 2 == 0:
        print(word, end=" ")
