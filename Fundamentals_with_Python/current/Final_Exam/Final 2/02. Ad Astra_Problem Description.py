import re
text = input()
pattern = r'(\||#)([a-zA-z\s]*)\1(\d{2}\/\d{2}\/\d{2})\1((?:[0-9]\d{0,3}|10000))\1'
matches = re.finditer(pattern, text)

foods = {}
total_cal = 0
for match in matches:
    food = match[2]
    expiration = match[3]
    cal = int(match[4])
    foods[food] = {"expiration": expiration, "calories": cal}
    total_cal += cal
print(f'You have food to last you for: {total_cal // 2000} days!')

for food, data in foods.items():
    print(f'Item: {food}, Best before: {data["expiration"]}, Nutrition: {data["calories"]}')
