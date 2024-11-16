class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions: list = []

    def handle_transaction(self, transaction_amount: int) -> str:
        to_handle = self.amount + transaction_amount
        if to_handle >= 0:
            self.amount = to_handle
            self._transactions.append(transaction_amount)
            return f'New balance: {self.amount}'
        else:
            raise ValueError('sorry cannot go in debt!')

    def add_transaction(self, amount: int) -> str:
        if isinstance(amount, int):
            return self.handle_transaction(amount)
        else:
            raise ValueError('please use int for amount')

    def balance(self):
        return sum(self._transactions) + self.amount

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
