string_first = input()
string_second = input()

while string_first in string_second:
    string_second = string_second.replace(string_first, "")
print(string_second)
