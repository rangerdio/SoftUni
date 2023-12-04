last_sector = input()
first_sector_rows = int(input())
seat_odd_quantity = int(input())
seat_odd = 97 + seat_odd_quantity
seat_even = seat_odd + 2
last_sector_num = ord(last_sector)
odd_counter = 0
even_counter = 0
for sector in range(65, last_sector_num + 1):
    for rows in range(1, first_sector_rows + 1):
        if rows % 2 != 0:
            for seat in range(97, seat_odd):
                print(f"{chr(sector)}{rows}{chr(seat)}")
                odd_counter += 1
        else:
            for seat in range(97, seat_even):
                print(f"{chr(sector)}{rows}{chr(seat)}")
                even_counter += 1
    first_sector_rows += 1
print(odd_counter + even_counter)

for 