def loading_bar(number: int):
    complete = (number // 10) * "%"
    incomplete = (10 - number // 10) * "."
    if number < 100:
        return f"{number}% [{complete}{incomplete}]\nStill loading..."
    else:
        return f"100% Complete!\n[{complete}{incomplete}]"


number_int = int(input())
print(loading_bar(number_int))
