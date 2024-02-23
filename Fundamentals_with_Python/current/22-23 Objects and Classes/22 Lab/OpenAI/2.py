# 10 SIMPLE TASK FROM OpenAI

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit_(self, amount_):
        self.balance += amount_
        print(f"Deposit {amount_}")

    def withdraw_(self, amount_):
        if self.balance >= amount_:
            self.balance -= amount_
            print(f"Withdraw {amount_}")
        else:
            print("Not enough balance to withdraw!")


account = BankAccount(0) # starting balance 0


while True:
    command = input()
    if command == "Stop":
        break
    command = command.split()
    amount = int(command[1])
    if command[0] == "deposit":
        account.deposit_(amount)
    elif command[0] == "withdraw":
        account.withdraw_(amount)


print(f"Final account balance is {account.balance}")

# 2. Problem Description:
# Create a class called BankAccount with attribute balance. Implement methods deposit and withdraw to modify the balance.
#
#
# PyCharm Test and Answers:
#
# account = BankAccount()
# account.deposit(100)
# account.withdraw(50)
# print(account.balance)
#
# Expected output: 50
#
#
# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Insufficient funds")
