text = input()
data = []
hits = {}
for index,letter in enumerate(text):
    data.append(letter)

for element in data:
    if element not in hits:
        hits[element] = data.count(element)
for element, hits in hits.items():
    print(f"{element}: {hits} time/s")
