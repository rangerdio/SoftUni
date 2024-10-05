hriz = int(input())
roses = int(input())
tulip = int(input())
season = input()
holiday = input()
hriz_price = 0
roses_price = 0
tulip_price = 0

if holiday == "Y":
    holiday = 1.15
elif holiday == "N":
    holiday = 1

if season == "Spring" or season == "Summer":
    hriz_price = 2 * holiday
    roses_price = 4.10 * holiday
    tulip_price = 2.50 * holiday
elif season == "Autumn" or season == "Winter":
    hriz_price = 3.75 * holiday
    roses_price = 4.50 * holiday
    tulip_price = 4.15 * holiday
bouquet_price = roses_price * roses + hriz_price * hriz + tulip_price * tulip

if tulip > 7 and season == "Spring":
    bouquet_price = bouquet_price * 0.95
if roses >= 10 and season == "Winter":
    bouquet_price = bouquet_price * 0.90
if hriz + roses + tulip > 20:
    bouquet_price = bouquet_price * 0.80
bouquet_price = bouquet_price + 2
print(f"{bouquet_price:.2f}")
