inheritance = float(input())
year_to_live = int(input())
start_year = 1800
age = 17


for number in range(1800, year_to_live + 1):
    age +=1
    if number % 2 == 0:
        inheritance -= 12000
    else:
       inheritance -= 12000 + 50 * age

if inheritance >= 0:
    print(f"Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.")
else:
    print(f"He will need {abs(inheritance):.2f} dollars to survive.")
