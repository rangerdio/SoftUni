# from copy import deepcopy
#
# sub_list = [1, 2]
# sub_list_2 = [3, 4]
# a = [sub_list, sub_list_2]
# b = a.copy()
# print(a)
# print(b)
#
# a[0].append(100)
# print(a)
# print(b)
# c = deepcopy(a)
# print(c)


# koko = (1, 10, 3, 4, 5, 6, 7, 8, 9, 10)
# print(koko[-1])
#
# print(koko.count(10))
#
#
# print(koko.index(10))

# text = "hello"
# text += "!"
# print(text)

a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])

print("union, ", a | b)
print("union, ", a.union(b))

print("intersection, ", a & b)
print("intersection, ", a.intersection(b))

print("difference, ", a - b)
print("difference, ", a.difference(b))

print("symmetric difference, ", a ^ b)
print("symmetric difference, ", a.symmetric_difference(b))

print("subset, ", a < b)
print("subset, ", a.issubset(b))

print("superset, ", a > b)
print("superset, ", a.issuperset(b))




# Unique elements - set
# different elements which to modify and add - list
# read only collection - Tupple
# key value pair - Dictionary



tag = (1, 2, 3, 4, 5, 6, 7, 9, 0)
print(tag)