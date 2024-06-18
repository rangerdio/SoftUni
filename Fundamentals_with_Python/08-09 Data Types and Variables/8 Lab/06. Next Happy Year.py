year = int(input())
while True:
    year += 1
    year_str = str(year)
    uniq = set(year_str)
    if len(uniq) == len(year_str):
        print(uniq)
        break
print(year)

# year = int(input())
# year_str = str(year)
# len_ = len(year_str)
# if len_ == 3:
#     while True:
#         year += 1
#         if year_str[0] != year_str[1] and year_str[0] != year_str[2] \
#                 and year_str[1] != year_str[2]:
#             break
#
# elif len_ == 2:
#     while True:
#         year += 1
#         if year_str[0] != year_str[1]:
#             break
# elif len_ == 1:
#     year += 1
#
#
# elif len_ == 4:
#     while True:
#         year += 1
#         if year_str[0] != year_str[1] and year_str[0] != year_str[2] and year_str[0] != year_str[3] \
#                 and year_str[1] != year_str[2] and year_str[1] != year_str[3] and year_str[2] != year_str[3]:
#             break
# elif len_ == 5:
#     while True:
#         year += 1
#         if year_str[0] != year_str[1] and year_str[0] != year_str[2] and year_str[0] != year_str[3] and year_str[0] != year_str[4]\
#                 and year_str[1] != year_str[2] and year_str[1] != year_str[3] and year_str[1] != year_str[4]\
#                 and year_str[2] != year_str[3] and year_str[2] != year_str[4] and year_str[3] != year_str[4]:
#             break
# print(year_str)
