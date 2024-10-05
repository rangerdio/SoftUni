try:
    with open('text.txt', 'r') as _:
        print('File found')
except FileNotFoundError:
    print("File not found")
