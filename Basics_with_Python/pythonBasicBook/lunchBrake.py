import math
serial_name = input()
epizod_time = int(input())
brake_time = int(input())

lunch_time = brake_time / 8
resting_time = lunch_time * 2
required_time = lunch_time + resting_time + epizod_time
if required_time <= brake_time:
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(brake_time - required_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(required_time - brake_time)} more minutes.")
    