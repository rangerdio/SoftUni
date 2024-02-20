def rounding(string: str):
    float_list = list(map(float, string.split()))
    rounded_list = []
    for element in float_list:
        rounded_list.append(round(element))
    return rounded_list


print(rounding(input()))
