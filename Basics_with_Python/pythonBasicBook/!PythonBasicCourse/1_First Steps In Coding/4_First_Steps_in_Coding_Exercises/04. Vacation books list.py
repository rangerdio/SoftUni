import math

current_book_pages = int(input())
pages_per_hour = int(input())
given_days = int(input())

needed_hours_per_book =  current_book_pages / pages_per_hour
hour_per_day = needed_hours_per_book // given_days
print(hour_per_day)