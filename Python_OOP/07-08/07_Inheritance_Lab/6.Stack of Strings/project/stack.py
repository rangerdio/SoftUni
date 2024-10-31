class Stack:
    def __init__(self, *args):
        self.data: list = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self) -> str:
        return '[' + ', '.join(self.data[::-1]) + ']'
        # return f'{self.data}'


data = Stack()

# data.push('1')
# data.push('22')
# data.push('333')
# data.push('444')
# print(data)
# data.pop()
# print(data)
# data.pop()
# print(data)
# data.pop()
# print(data)
# print(data.is_empty())
# data.pop()
# print(data)
# print(data.is_empty())

data.push("apple")
data.push("carrot")
print(str(data))
# self.assertEqual(str(data), '[carrot, apple]')
# self.assertEqual(data.pop(), 'carrot')
data.pop()
print(data)
# self.assertEqual(data.top(), 'apple')
print(data.top(), 'apple')
data.push("cucumber")
print(data)
# self.assertEqual(str(data), '[cucumber, apple]')
# self.assertEqual(data.is_empty(), False)
