weather =  float(input())

if weather >= 26.00 and weather <= 35.00:
    print("Hot")
elif weather >= 20.1 and weather <= 25.9:
    print("Warm")
elif weather >= 15.00 and weather <= 20.00:
    print("Mild")
elif weather >= 12.00 and weather <= 14.9:
    print("Cool")
elif weather >= 5.00 and weather <= 11.9:
    print("Cold")
else:
    print("unknown")
