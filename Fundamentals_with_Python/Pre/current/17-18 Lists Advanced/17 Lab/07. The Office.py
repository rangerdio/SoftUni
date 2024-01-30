happiness_list = list(map(int, input().split(" ")))
improvement_factor = int(input())

happiness_list_factored = [element * improvement_factor for element in happiness_list if element / element == 1]
# print(happiness_list_factored)
average = 0

for element in happiness_list_factored:
    average += element
average = average / len(happiness_list_factored)

happy = sum(1 for element in happiness_list if element >= average)
not_happy = sum(1 for element in happiness_list if element < average)

print(f"Score: {happy}/{happy}+{not_happy}. Employees are happy!") if happy >= not_happy else print(f"Score: {happy}/{happy}+{not_happy}. Employees are not happy!")
