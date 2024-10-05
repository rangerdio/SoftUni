num = int(input())
day = input()
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
    if num < 10 or num >= 18:
        print("closed")
    else:
        print("open")
elif day == "Sunday":
    if num < 10 or num >= 18:
        print("closed")
    else:
        print("open")