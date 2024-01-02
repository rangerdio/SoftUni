def calculations(operator: str, param1: int, param2: int):
    if operator == "multiply":
        return param1 * param2
    elif operator == "divide":
        return int(param1 / param2)
    elif operator == "add":
        return param1 + param2
    elif operator == "subtract":
        return param1 - param2


operation = str(input())
value_1 = int(input())
value_2 = int(input())
print(calculations(operation, value_1, value_2))
