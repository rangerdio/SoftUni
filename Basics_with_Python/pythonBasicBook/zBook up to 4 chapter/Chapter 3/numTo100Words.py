number = int(input("Enter number between 0 and 100: "))

if number > 9 and number < 100:
    firstDigit = number // 10
    secondDigit = number % 10
    if firstDigit == 1:
        if secondDigit == 1:
            print("eleven")
        elif secondDigit == 2:
            print("twelve")
        elif secondDigit == 3:
            print("thirdteen")
        elif secondDigit == 4:
            print("fourteen")
        elif secondDigit == 5:
            print("fiveteen")
        elif secondDigit == 6:
            print("sixteen")
        elif secondDigit == 7:
            print("seventeen")
        elif secondDigit == 8:
            print("eighteen")
        elif secondDigit == 9:
            print("ninetheen")



elif number == 100:
    print("one hundred")

