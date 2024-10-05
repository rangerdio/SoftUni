import math
hours_needed = int(input())
days_given = int(input())
employees = int(input())

total_given_hours = math.floor(days_given * 8 * employees)
overtime_hours = math.floor(days_given * employees * 2)
total_hours_without_training = math.floor(overtime_hours + total_given_hours * 0.9)

if total_hours_without_training >= hours_needed:
    print(f"Yes!{(abs(total_hours_without_training - hours_needed))} hours left.")
else:
    print(f"Not enough time!{math.floor(abs(total_hours_without_training - hours_needed))} hours needed.")
import math
hours_needed = int(input())
days_given = int(input())
employees = int(input())

total_given_hours = math.floor(days_given * 8 * employees)
overtime_hours = math.floor(days_given * employees * 2)
total_hours_without_training = math.floor(overtime_hours + total_given_hours * 0.9)

if total_hours_without_training >= hours_needed:
    print(f"Yes!{(abs(total_hours_without_training - hours_needed))} hours left.")
else:
    print(f"Not enough time!{math.floor(abs(total_hours_without_training - hours_needed))} hours needed.")
