def collect(data_to_collect: list):
    results = {}
    for index in range(0, len(data_to_collect), 2):
        key = data_to_collect[index]
        quantity = data_to_collect[index + 1]

        if key not in results.keys():
            results[key] = int(quantity)
        else:
            results[key] += int(quantity)

    return [print(f"{resource_} -> {quantity_}") for resource_, quantity_ in results.items()]


resources = []
while True:
    # resource_to_collect: str, quantity: int
    command = input()
    if command == "stop":
        break
    resource = command
    value = input()
    resources.append(resource)
    resources.append(value)

collect(resources)
