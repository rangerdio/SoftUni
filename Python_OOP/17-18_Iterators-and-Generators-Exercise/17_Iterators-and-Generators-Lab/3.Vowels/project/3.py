class vowels:
    def __init__(self, string: str):
        self.string = [letter for letter in string if letter.lower() in 'aoueiy']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.string):
            raise StopIteration
        return self.string[self.index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
