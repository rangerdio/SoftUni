class countdown_iterator:
    def __init__(self, count: int):
        self.count = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 1:
            raise StopIteration
        self.count -= 1
        return self.count


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
