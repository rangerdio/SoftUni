energy = int(input())
# if start energy = 0  print "Not enough energy! Game ends with 0 won battles and 0 energy".
target_energy_need_distance = 0
while energy > 0:
    command = input()
    if command == "End of battle":
        pass
    else:
        target_energy_need_distance = int(command)
    if energy >= target_energy_need_distance:





    pass



