countries, capitals = input().split(", "), input().split(", ")
dictionary = dict(zip(countries, capitals))
[print(f"{key} -> {value}") for key, value in dictionary.items()]
