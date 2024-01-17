
# test = lambda x: x + 10
# print(test(5))
#
# summ = lambda a, b: a + b
# subtract = lambda a, b: a - b
# multiply = lambda a, b: a * b
# divide = lambda a, b: a / b
# print(summ(3, 2))
# print(subtract(3, 2))
# print(multiply(3, 2))
# print(divide(3, 2))
#

# list1 = [5, 3, 1, 4, 2]
# sort = sorted(list1, key=lambda x: x)
# print(sort)
# sort2 = sorted(list1, key=lambda x: x, reverse=True)
# print(sort2)

# list2 = [1, 2, 3, 4, 5, 6]
# filtered_list = list(filter(lambda x: x > 3, list2))
# print(filtered_list)

# list4 = [1, 2, 3, 4, 5]
# square = list(map(lambda x: x**2, list4))
# print(square)

# string = "hello world"
# cap_words = map(lambda word: word.capitalize(), string.split())
# cap_string = ' '.join(cap_words)
# print(cap_string)
#
# asd = "ivan".capitalize()
# print(asd)


# check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(check_even_odd(6))
# print(check_even_odd(7))

# num = [1, 2, 3]
# sq = [x ** 2 for x in num if x > 1]
# print(sq)

print([num for num in range(11) if num % 2 == 0])


