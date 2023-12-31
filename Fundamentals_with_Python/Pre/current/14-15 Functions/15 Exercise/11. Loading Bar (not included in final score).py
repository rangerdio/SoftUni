def loading_bar(number: int):
    complete = (number // 10) * "%"
    incomplete = (10 - number // 10) * "."
    complete_bar = number + "% [" + complete + incomplete + "]"
    return


number_int = int(input())
print(loading_bar(number_int))
