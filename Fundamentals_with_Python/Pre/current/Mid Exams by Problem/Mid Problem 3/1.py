def index_validation(data_list: list, index: int):
    valid_list = []
    for _ in range(len(data_list)):
        valid_list.append(_)
    if index in valid_list:
        return True
    else:
        return False


asd = [1, 2, 3, 4, 5]

if index_validation(asd, 4):
    print(f"asd")
else:
    print(f"kuku")
