countries = input().split(", ")
capitals = input().split(", ")
pairs = dict(zip(countries, capitals))
for country, capital in pairs.items():
    print(f"{country} -> {capital}")
