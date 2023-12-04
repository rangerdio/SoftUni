movie_name = input()
total_tickets_sold = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
while movie_name != "Finish":
    capacity = int(input())
    sold_tickets = 0
    for sold in range(1, capacity + 1):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        sold_tickets = sold
    all_sold = (sold_tickets / capacity) * 100
    print(f"{movie_name} - {all_sold:.2f}% full.")
    movie_name = input()
total_tickets_sold = student_tickets + standard_tickets + kid_tickets
total_student = student_tickets / total_tickets_sold * 100
total_standard = standard_tickets / total_tickets_sold * 100
total_kid = kid_tickets / total_tickets_sold * 100
print(f"Total tickets: {total_tickets_sold}")
print(f"{total_student:.2f}% student tickets.")
print(f"{total_standard:.2f}% standard tickets.")
print(f"{total_kid:.2f}% kids tickets.")
