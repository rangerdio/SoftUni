class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml: int, capacity=capacity) -> str:
        if self.content + ml <= capacity:
            self.content += ml
            return f'Glass filled with {ml} ml'
        return f'Cannot add {ml} ml'

    def empty(self) -> str:
        self.content = 0
        return "Glass is now empty"

    def info(self, capacity=capacity) -> str:
        return f'{capacity - self.content} ml left'


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
