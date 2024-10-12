def accommodate_new_pets(capacity, max_weight, *pet_data):
    pets = {}
    all_pets = len(pet_data)
    acc = 0
    for pet_type, weight in pet_data:
        if capacity > 0:
            acc += 1
            if weight > max_weight:
                continue
            else:
                if pet_type not in pets:
                    pets[pet_type] = 0
                pets[pet_type] += 1
                capacity -= 1

        else:
            break
    if acc == all_pets:
        result = f'All pets are accommodated! Available capacity: {capacity}.\n'
    else:
        result = 'You did not manage to accommodate all pets!\n'
    sorted_pets = sorted(pets.items(), key=lambda x: x[0])
    result += 'Accommodated pets:\n'

    for pet_type, count in sorted_pets:
        result += f'{pet_type}: {count}\n'
    return result


# print(accommodate_new_pets(
#     10,
#     15.0,
#     ("cat", 5.8),
#     ("dog", 10.0),
# ))
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
# print(accommodate_new_pets(
#     2,
#     15.0,
#     ("dog", 10.0),
#     ("cat", 5.8),
#     ("cat", 2.7),
# ))
