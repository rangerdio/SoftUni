string = input()
list_ = []

# for index, letter in enumerate(string):
#     if ord(letter) < 97:
#         list_.append(index)

for i in range(len(string)):
    if string[i].isupper():
        list_.append(i)

print(list_)
