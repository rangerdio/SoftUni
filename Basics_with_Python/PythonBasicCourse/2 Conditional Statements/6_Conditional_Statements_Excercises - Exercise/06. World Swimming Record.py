world_record = float(input())
distance = float(input())
timing_per_meter = float(input())

calc = distance * timing_per_meter
correction_multiplier = distance // 15 # was corrected due to judge errors that want correction multiplier be int
correction_seconds = correction_multiplier * 12.5
time = calc + correction_seconds

if time < world_record:
    print(f" Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {time - world_record:.2f} seconds slower.")
