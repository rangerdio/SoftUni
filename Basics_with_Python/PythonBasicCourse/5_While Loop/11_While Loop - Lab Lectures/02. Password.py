# username = input()
# password = input()
# current_password = input()
# while current_password != password:
#     current_password = input()
# print(f"Welcome {username}!")


username = input()
password = input()
while True:
    current_password = input()
    if current_password == password:
        print(f"Welcome {username}!")
        break
