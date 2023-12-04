import math
print(" Wide of the room must be equar or more than 3 meters! \n Lenght of the room must not exceed 100 meters! \n Lenght must be more than Wide \n")

l = float(input("Enter Lenght of the room in meters :"))
w = float (input("Enter Wide of th room in meters:"))
if l >= 100:
    print ("Your Lenght not pass the requirements. Entered Value: ",l)
elif l<=0:
    print("Your Lenght can not take negative value or be 0. Entered Value: ",l)
elif w <= 0:
    print("Your Wide can not take negative value or be 0. Entered Value: ",w)
elif w <=3:
    print("Your Wide not pass the requirements. Entered Value: ", w)
elif w>l:
    print (f"Wide value must not be bigger than Lenght value! w= {w} l= {l}")
else:
    seat_l = 1.2
    seat_w = 0.7
    max_row = math.floor(l/seat_l)
    max_col = math.floor ((w-1)/seat_w)
    max_seats = max_col*max_row -3
    print(max_seats)