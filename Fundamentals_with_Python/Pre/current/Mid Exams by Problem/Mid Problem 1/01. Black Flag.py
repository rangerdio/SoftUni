
total_days_pirating = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
current_day = 1
total_plunder = 0

while current_day <= total_days_pirating:
    plunder_current_day = daily_plunder * 1.5 if current_day % 3 == 0 else daily_plunder
    total_plunder += plunder_current_day
    if current_day % 5 == 0:
        total_plunder *= 0.7
    current_day += 1

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {(100 * total_plunder / expected_plunder):.2f}% of the plunder.")
