# cities = 10
# for num in range(1, cities + 1):
#     print(num)


def last(phone_list: list, phone: str):
    print(f"start list: {phone_list}")
    if phone in phone_list:
        # index = phone_list.index(phone)
        # phone_list.append(phone_list.pop(index))    # MULTI NOT considered
        hits = phone_list.count(phone)
        for i in range(hits):
            phone_list.remove(phone)
            print(f"remove result: {hits}, {phone_list}")
        for i in range(hits):
            phone_list.insert(-1, phone)
            print(f"append result: {hits}, {phone_list}")

    return phone_list

# def last(phone_list: list, phone: str):
#     print(f"start list: {phone_list}")
#     if phone in phone_list:
#         hits = phone_list.count(phone)
#         for _ in range(hits):
#             phone_list.remove(phone)
#             print(f"remove result: {phone_list}")
#         for _ in range(hits):
#             phone_list.append(phone)
#             print(f"append result: {phone_list}")
#
#     return phone_list


asd = "SamsungA50, MotorolaG5, SamsungA50, HuaweiP10".split(", ")

print(last(asd, "SamsungA50"))
