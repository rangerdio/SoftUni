#  import math
percent = 0
parcel_weight = float(input())
service_type = input()
distance = int(input())
price_per_km = 0
adds_total = 0
if service_type == "standard":
    if parcel_weight < 1:
        price_per_km = 0.03
    elif 1 <= parcel_weight < 10:
        price_per_km = 0.05
    elif 10 <= parcel_weight < 40:
        price_per_km = 0.10
    elif 40 <= parcel_weight < 90:
        price_per_km = 0.15
    elif 90 <= parcel_weight < 150:
        price_per_km = 0.20
elif service_type == "express":
    if parcel_weight < 1:
        price_per_km = 0.03
        percent = 80
    elif 1 <= parcel_weight < 10:
        price_per_km = 0.05
        percent = 40
    elif 10 <= parcel_weight < 40:
        price_per_km = 0.10
        percent = 5
    elif 40 <= parcel_weight < 90:
        price_per_km = 0.15
        percent = 2
    elif 90 <= parcel_weight < 150:
        price_per_km = 0.20
        percent = 1

needed_money = distance * price_per_km
if service_type == "standard":
    needed_money = distance * price_per_km
    print(f"The delivery of your shipment with weight of {parcel_weight:.3f} kg. would cost {needed_money:.2f} lv.")
elif service_type == "express":

    adds_per_kg = price_per_km * percent / 100
    adds_per_km = adds_per_kg * parcel_weight
    adds_total = distance * adds_per_km

    needed_money = distance * price_per_km + adds_total
    print(f"The delivery of your shipment with weight of {parcel_weight:.3f} kg. would cost {needed_money:.2f} lv.")
