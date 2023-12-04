saves = 0
destination = input()
budged = float(input())
while destination != "End":
    save = float(input())
    saves += save
    if saves >= budged:
        print(f"Going to {destination}!")
        destination = input()
        if destination == "End":
            break
        budged = float(input())
        saves = 0
