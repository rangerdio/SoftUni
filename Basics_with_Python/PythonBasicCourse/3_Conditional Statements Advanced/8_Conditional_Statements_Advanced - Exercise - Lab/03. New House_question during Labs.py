# Условието не е зададено коректно.
# Условностите са тези:
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
#
# Пример: Ако Нели купи 100 рози, то тя получава 10 % отстъпка от крайната цена. Понеже е закупила рози,
# то тя няма отстъпка за Далии и Лалета, обаже има допълнително оскъпяване за това че е закупила 0 Нарциса < 120 и 0 Гладиоли < 80
#
# За зададените отговори в Judge, условието би следвало да е така:
# •	Ако Нели купи Нарциси, и те са по-малко от 120  - цената се оскъпява с 15%;
# •	Ако Нели Купи Гладиоли, и те са по-малко от 80  - цената се оскъпява с 20%.


type_flower = input()
quantity = int(input())
budged = int(input())
total = 0
if type_flower == "Roses":
    if quantity > 80:
        total = quantity * 5 * 0.90
    else:
        total = quantity * 5
elif type_flower == "Dahlias":
    if quantity > 90:
        total = quantity * 3.80 * 0.85
    else:
        total = quantity * 3.80
elif type_flower == "Tulips":
    if quantity > 80:
        total = quantity * 2.80 * 0.85
    else:
        total = quantity * 2.80
elif type_flower == "Narcissus":
    if quantity < 120:
        total = quantity * 3.00 * 1.15
    else:
        total = quantity * 3.00
elif type_flower == "Gladiolus":
    if quantity < 80:
        total = quantity * 2.5 * 1.20
    else:
        total = quantity * 2.50
difference = abs(budged - total)
if budged >= total:
    print(f"Hey, you have a great garden with {quantity} {type_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
