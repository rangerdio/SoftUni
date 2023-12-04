import math
mm = int(input())
ss = int(input())
length_m = float(input())
seconds_per_100 = float(input())

control = mm * 60 + ss
kolko_puti = length_m / 120
namaleno_vreme = kolko_puti * 2.5

time = length_m / 100 * seconds_per_100 - namaleno_vreme


if time <= control:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    print(f"No, Marin failed! He was {(time - control):.3f} second slower.")
