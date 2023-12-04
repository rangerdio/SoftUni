import math
hours_needed = int(input())
days_given = int(input())
employees = int(input())

overtime_hours = math.floor(days_given * employees * 2)
total_hours_without_training = math.floor((days_given * employees * 8 + overtime_hours) * 0.9)


if total_hours_without_training >= hours_needed:
    print(f"Yes!{(abs(total_hours_without_training - hours_needed))} hours left.")
else:
    print(f"Not enough time!{math.floor(abs(total_hours_without_training - hours_needed))} hours needed.")
