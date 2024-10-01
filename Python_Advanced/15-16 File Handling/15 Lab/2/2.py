with open('numbers.txt', 'r') as numbers:
    content = [int(x) for x in numbers.read().split('\n')]
    print(sum(content))
