class MoneyNotEnoughError (Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


AGE_MIN = 18
params = input().split(', ')
PIN = params[0]
BALANCE = float(params[1])
age = int(params[2])

while True:
    user_input = input()
    if user_input == 'End':
        break
    command_list = user_input.split('#')
    command = command_list[0]
    money = float(command_list[1])

    if command == 'Send Money':
        pin = command_list[2]

        if not money <= BALANCE:
            raise MoneyNotEnoughError('Insufficient funds for the requested transaction')
        if pin != PIN:
            raise PINCodeError('Invalid PIN code')
        if age < AGE_MIN:
            raise UnderageTransactionError('You must be 18 years or older to perform online transactions')
        print(f'Successfully sent {money:.2f} money to a friend')
        print(f'There is {(BALANCE - money):.2f} money left in the bank account')

    elif command == 'Receive Money':
        if money < 0:
            raise MoneyIsNegativeError('The amount of money cannot be a negative number')
        print(f'{money/2:.2f} money went straight into the bank account')
