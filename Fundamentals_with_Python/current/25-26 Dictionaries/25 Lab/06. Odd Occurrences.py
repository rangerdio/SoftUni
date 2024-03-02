element_list = input().split()
elements = {}
# elements_list_lowered = []
# [elements_list_lowered.append(word.lower()) for word in element_list]

for word in element_list:
    if word.lower() not in elements.keys():
        elements[word.lower()] = 0
    elements[word.lower()] += 1

for word, value in elements.items():
    if value % 2 == 0:
        print(word, end=" ")
