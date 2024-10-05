movie_name = input()
total_ticket_cnt = 0
student_ticket_cnt = 0
standard_ticket_cnt = 0
kid_ticket_cnt = 0

while movie_name != "Finish":
    available_seats = int(input())
    seats_cnt = 0
    for seat in range(available_seats):
        seat_type = input()
        if seat_type == "End":
            break
        seats_cnt += 1
        if seat_type == "student":
            student_ticket_cnt += 1
        elif seat_type == "standard":
            standard_ticket_cnt += 1
        elif seat_type == "kid":
            kid_ticket_cnt += 1

    total_ticket_cnt += seats_cnt
    seats = 100 * seats_cnt / available_seats
    print(f"{movie_name} - {seats:.2f}% full.")

    movie_name = input()
students = 100 * student_ticket_cnt / total_ticket_cnt
standards = 100 * standard_ticket_cnt / total_ticket_cnt
kids = 100 * kid_ticket_cnt / total_ticket_cnt

print(f"Total tickets: {total_ticket_cnt}")
print(f"{students:.2f}% student tickets.")
print(f"{standards:.2f}% standard tickets.")
print(f"{kids:.2f}% kids tickets.")
