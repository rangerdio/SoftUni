def forecast(*location_data):
    locations_sunny = {}
    locations_other = {}
    for location, weather in location_data:
        if weather == "Sunny":
            locations_sunny[location] = weather
        else:
            locations_other[location] = weather
    locations_sunny_ordered = sorted(locations_sunny.items(), key=lambda x: x[0])
    locations_other_ordered = sorted(locations_other.items(), key=lambda x: (x[1], x[0]))
    result = ""
    if locations_sunny_ordered:
        for location, weather in locations_sunny_ordered:
            result += f"{location} - {weather}\n"
    if locations_other_ordered:
        for location, weather in locations_other_ordered:
            result += f"{location} - {weather}\n"
    return result

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
