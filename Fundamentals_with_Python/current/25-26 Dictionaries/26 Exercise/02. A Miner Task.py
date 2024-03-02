def collect(data_to_collect: list):
    pass


resources = []
while True:
    # resource_to_collect: str, quantity: int
    command = input()
    if command[0] == "stop":
        break
    resource = command
    value = int(input())
    resources.append(input().split())

print(collect(resources))
