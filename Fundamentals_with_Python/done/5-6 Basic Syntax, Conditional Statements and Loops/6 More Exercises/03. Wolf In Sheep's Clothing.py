string_ = input()
animal_list = string_.split()
sheep_cnt = 0
for i in range((len(animal_list) - 1), -1, -1):
    if animal_list[i] == "wolf" and i == len(animal_list) - 1:
        print("Please go away and stop eating my sheep")
    elif animal_list[i] == "sheep" or animal_list[i] == "sheep," or animal_list[i] == "sheep, ":
        sheep_cnt += 1
    elif animal_list[i] == "wolf,":
        print(f"Oi! Sheep number {sheep_cnt}! You are about to be eaten by a wolf!")
