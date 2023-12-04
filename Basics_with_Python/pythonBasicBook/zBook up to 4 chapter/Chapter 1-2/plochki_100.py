import math
side = float(input())
l_plochka = float(input())
w_plochka = float(input())
l_peika = float(input())
w_peika = float(input())
time_plochka = 0.2
area=side*side
area_plochka = l_plochka * w_plochka
area_peika = l_peika*w_peika
broi = (area - area_peika) / area_plochka
time_all = broi*0.2
print(round(broi,2))
print(round(time_all,2))

