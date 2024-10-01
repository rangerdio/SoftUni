with open('text.txt', 'r') as my_file:
    for index, data in enumerate(my_file.readlines()):
        if index % 2 == 0:
            data = data.strip()
            for char in ("-", ",", ".", "!", "?"):
                if char in data:
                    data = data.replace(char, '@')
            reversed_data = " ".join(data.split()[::-1])
            print(reversed_data)
