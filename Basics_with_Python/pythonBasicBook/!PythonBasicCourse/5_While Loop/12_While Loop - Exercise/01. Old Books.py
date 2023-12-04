# needed_book = input()
# book_count = 0
# found = False
# not_found = False
# while True:
#     book = input()
#     if book == needed_book:
#         found = True
#         break
#     elif book == "No More Books":
#         not_found = True
#         break
#     book_count += 1
# if found:
#     print(f"You checked {book_count} books and found it.")
# elif not_found:
#     print(f"The book you search is not here!")
#     print(f"You checked {book_count} books.")

needed_book = input()
book_count = 0
found = False
not_found = False
book = input()
while book != needed_book:
    if book == "No More Books":
        not_found = True
        break
    book_count += 1
    book = input()

if not_found:
    print(f"The book you search is not here!")
    print(f"You checked {book_count} books.")
else:
    print(f"You checked {book_count} books and found it.")
