import re
locations = input()

pattern = r''
valid_locations = re.findall(pattern, locations)
print(locations)

points = 0
for location in locations:
    points += len(location)

print(f'Destinations: {", ". join(locations)}')
print(f'Travel Points: {points}')
