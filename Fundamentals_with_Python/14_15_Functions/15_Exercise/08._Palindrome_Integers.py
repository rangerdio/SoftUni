def is_palindrome(my_int):
    my_str = str(my_int)
    return my_str == my_str[::-1]


def palindrome(my_int_list):
    for element in range(len(my_int_list)):
        print(is_palindrome(my_int_list[element]))
        # print(type(my_int_list[element]))
    return


string = input()
numbers = list(map(int, string.split(", ")))
palindrome(numbers)
