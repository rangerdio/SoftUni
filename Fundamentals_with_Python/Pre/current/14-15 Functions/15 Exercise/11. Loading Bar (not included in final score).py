def loading_bar(number: int):
    complete = number // 10
    incomplete = 10 - complete
    print(complete)
    print(incomplete)
    return


number_int = int(input())
print(loading_bar(number_int))
