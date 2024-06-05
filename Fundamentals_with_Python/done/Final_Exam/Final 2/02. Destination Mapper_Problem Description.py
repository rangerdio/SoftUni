import re
locations = input()
pattern = r'(=|\/)([A-Z]{1}[A-Za-z]{2,})\1'
valid_locations = list(re.finditer(pattern, locations))

locations = []
points = 0
for match in valid_locations:
    location = match.group(2)
    locations.append(location)
    points += len(location)

print(f'Destinations: {", ". join(locations)}')
print(f'Travel Points: {points}')
