import math
world_record = float(input())
distance = (float(input()))
time_sec_m = float(input())

ivan_time = distance * time_sec_m

correction_time = (math.floor(distance / 15)) * 12.5
ivan_time_new = ivan_time + correction_time

if ivan_time_new < world_record:
    print(f"Yes, he succeeded! The new world record is {ivan_time_new:.2f} seconds.")
else:
    print(f"No, he failed! He was {ivan_time_new - world_record:.2f} seconds slower.")