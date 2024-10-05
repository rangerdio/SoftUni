goal = 10000
step_counter = 0
steps_walked = input()

while True:
    if steps_walked == "Going home":
        break
    else:
        steps_walked = int(steps_walked)
        step_counter += steps_walked
        if step_counter >= goal:
            print("Goal reached! Good job!")
            print(f"{step_counter - goal} steps over the goal!")
            break
        steps_walked = input()

if steps_walked == "Going home":
    steps_walked = int(input())
    step_counter += steps_walked
    if step_counter < goal:
        print(f"{goal - step_counter} more steps to reach goal.")
    else:
        print("Goal reached! Good job!")
        print(f"{step_counter - goal} steps over the goal!")


#
# while steps_walked != "Going home":
#     steps_walked = int(steps_walked)
#     step_counter += steps_walked
#     if step_counter >= goal:
#         print("Goal reached! Good job!")
#         print(f"{step_counter - goal} steps over the goal!")
#         break
#     steps_walked = input()
#
# if steps_walked == "Going home":
#     steps_walked = int(input())
#     step_counter += steps_walked
#     if step_counter < goal:
#         print(f"{goal - step_counter} more steps to reach goal.")
#     else:
#         print("Goal reached! Good job!")
#         print(f"{step_counter - goal} steps over the goal!")
