from math import ceil
name = input()
episode_duration = int(input())
lunch_brake_duration = int(input())
eat_time = lunch_brake_duration / 8
rest_time = lunch_brake_duration / 4
tot_time = episode_duration + rest_time + eat_time


if tot_time <= lunch_brake_duration:
    print(f"You have enough time to watch {name} and left with {ceil(lunch_brake_duration - tot_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {ceil(tot_time - lunch_brake_duration)} more minutes.")
