poli = int(input())
paint = int(input())
razreditel = int(input())
hours = int(input())

price_poli = (poli + 2) * 1.5
price_pain = paint * 14.5 * 1.1
price_razreditel = razreditel * 5
adds = 0.4
total = price_razreditel + price_pain + price_poli + adds
workers = hours * total * 0.3
grand_total = total + workers
print(grand_total)
