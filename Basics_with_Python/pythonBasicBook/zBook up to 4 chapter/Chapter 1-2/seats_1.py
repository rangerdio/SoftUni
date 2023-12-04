import math
print(" Wide of the room must be equar or more than 3 meters! \n Lenght of the room must not exceed 100 meters! \n Lenght must be more than Wide \n")

l = float(input("Enter Lenght of the room in meters :"))
w = float (input("Enter Wide of th room in meters:"))
if l >= 100:
    print ("Your Lenght not pass the requirements. Entered Value: ",l)
elif l<=0:
    print("Your Lenght can not take negative value. Entered Value: ",l)
elif w < 0:
    print("Your Wide can not take negative value. Entered Value: ",w)
elif w <=3:
    print("Your Wide not pass the requirements. Entered Value: ", w)
elif w>l:
    print (f"Wide value must not be bigger than Lenght value! w= {w} l= {l}")
else:
    one_work_palce = 1.2*0.7
    door_and_teaching_place=3*one_work_palce
    coridor_area = 1.0*l
    room_area = l*w
    #print ("Room Area is : ",room_area)
    #print("Coridor area : ",coridor_area)
    #print("Door and Teaching place is:",door_and_teaching_place)
    #print("One workplace is : ",one_work_palce)
    workplace_area = room_area-coridor_area-door_and_teaching_place
    #print ("Maximum workplace area is: ",workplace_area)
    max_workplaces = workplace_area/one_work_palce
    #print("Maximum avaiable workplaces is: ",math.floor(max_workplaces))
    print (math.floor(max_workplaces))