number = input()
prime_sum = 0
not_prime_sum = 0
while number != "stop":
    number = int(number)
    if number < 0:
        print("Number is negative.")
        number = input()
        continue
    else:
        prime = True
        for check in range(2, number):
            if number % check == 0:
                prime = False
                break
        if prime:
            prime_sum += number
        else:
            not_prime_sum += number
        number = input()
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {not_prime_sum}")
