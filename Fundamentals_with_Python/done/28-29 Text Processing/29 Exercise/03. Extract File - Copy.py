path_elements = input().split("\\")
print(f'File name: {path_elements[-1].split(".")[0]}')
print(f'File extension: {path_elements[-1].split(".")[1]}')
