class sequence_repeat:
    def __init__(self,  sequence, number: int):
        self.sequence = sequence
        self.number = number
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration
        self.index = (self.index + 1) % len(self.sequence)
        self.number -= 1
        return self.sequence[self.index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
