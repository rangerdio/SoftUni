bitcoin = int(input())
ioan = float(input())
kom = float(input())
lv = bitcoin*1168
usd = ioan*0.15
lv2 = ioan*0.15*1.76
euro = (lv+lv2)/1.95
komisionna = euro*kom/100
reuro = round (euro-komisionna, 2)
print(reuro)

