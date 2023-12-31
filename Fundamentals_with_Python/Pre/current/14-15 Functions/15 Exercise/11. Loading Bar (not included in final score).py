def loading_bar(number: int):
    complete = (number // 10) * "%"
    incomplete = (10 - number // 10) * "."
    print(f" {number}% [{number * "%"}")
    return


number_int = int(input())
print(loading_bar(number_int))
