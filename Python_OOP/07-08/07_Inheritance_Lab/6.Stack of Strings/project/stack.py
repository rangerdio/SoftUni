class Stack:
    def __init__(self, data: list):
        self.data = data

    def push(self, element) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self):
        pass

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self) -> str:
        # return '[' + ', '.join(element for element in self.data) + ']'
        return f'{self.data}'


s = Stack([1, 22, 333])
s.push(444)
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
print(s.is_empty())
s.pop()
print(s)
print(s.is_empty())