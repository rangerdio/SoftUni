def loading_bar(number: int):
    complete = (number // 10) * "%"
    incomplete = (10 - number // 10) * "."
    return f"{number}% [{complete}{incomplete}]"


number_int = int(input())
print(loading_bar(number_int))
