path = input()
full_name = path.split("\\")[-1]
name = full_name.split(".")[0]
extension = full_name.split(".")[1]

print(f"File name: {name}")
print(f"File extension: {extension}")
