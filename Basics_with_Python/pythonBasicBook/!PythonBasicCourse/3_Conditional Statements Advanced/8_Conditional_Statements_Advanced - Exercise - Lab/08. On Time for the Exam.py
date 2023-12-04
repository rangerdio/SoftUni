exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_time_min = exam_hour * 60 + exam_min
arrival_time_min = arrival_hour * 60 + arrival_min
diff = abs(exam_time_min - arrival_time_min)
hh = diff // 60
mm = diff % 60

if exam_time_min - arrival_time_min == 0:
    print("On time")

elif (exam_time_min > arrival_time_min) and (abs(exam_time_min - arrival_time_min) < 31):
    print("On time")
    print(f"{mm} minutes before the start")

elif (exam_time_min > arrival_time_min) and (abs(exam_time_min - arrival_time_min) >= 31):
    print("Early")
    if hh == 0:
        print(f"{mm} minutes before the start")
    elif (hh != 0) and mm < 10:
        print(f"{hh}:0{mm} hours before the start")
    elif (hh != 0) and mm >= 10:
        print(f"{hh}:{mm} hours before the start")

elif exam_time_min < arrival_time_min:
    print("Late")
    if hh == 0:
        print(f"{mm} minutes after the start")
    elif (hh != 0) and mm < 10:
        print(f"{hh}:0{mm} hours after the start")
    elif (hh != 0) and mm >= 10:
        print(f"{hh}:{mm} hours after the start")
