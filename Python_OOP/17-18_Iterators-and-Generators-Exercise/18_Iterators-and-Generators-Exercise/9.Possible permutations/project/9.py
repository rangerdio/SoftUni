from itertools import permutations


def possible_permutations(iterable: list[int]):
    for permutation in permutations(iterable):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
