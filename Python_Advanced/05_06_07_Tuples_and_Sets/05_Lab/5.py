# number_of_guests = int(input())
# invitations = set()
# actual_guests = set()
#
# for _ in range(number_of_guests):
#     invitations.add(input())
#
# command = input()
# while command != "END":
#     actual_guests.add(command)
#     command = input()
#
# missing = invitations.difference(actual_guests)
#
#
# vip = []
# guests = []
# tag = (1, 2, 3, 4, 5, 6, 7, 9, 0)
#
# for element in missing:
#     if element[0] in tag:
#         vip.append(element)
#     else:
#         guests.append(element)
# vip.sort()
# guests.sort()
# print(len(missing), end='')
# print(*vip, sep='\n')
# print(*guests, sep='\n')

number_of_guests = int(input())
invitations = set()

for _ in range(number_of_guests):
    invitations.add(input())

command = input()
while command != "END":
    if command in invitations:
        invitations.remove(command)
    command = input()

sorted_invitations = sorted(invitations)
print(len(invitations))
print(*sorted_invitations, sep="\n")
