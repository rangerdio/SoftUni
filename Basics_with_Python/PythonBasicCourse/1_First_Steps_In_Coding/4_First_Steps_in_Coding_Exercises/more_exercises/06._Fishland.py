price_skumr = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())

price_palamud = 1.6 * price_skumr
price_safrid = 1.8 * price_caca
price_midi = 7.50
total = price_midi * kg_midi + price_safrid * kg_safrid + price_palamud * kg_palamud
print(f"{total:.2f}")
