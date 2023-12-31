def data_types(command_: str, data_: str):
    if command_ == "int":
        data_ = int(data_)
        return data_ * 2
    elif command_ == "real":
        data_ = float(data_) * 1.5
        return f"{data_:.2f}"
    elif command_ == "string":
        return f"${data_}$"
    return


command = input()
data = input()
print(data_types(command, data))
