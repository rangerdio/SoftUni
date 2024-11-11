class Customer:
    customer_id_counter = 1

    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.customer_id_counter
        Customer.customer_id_counter += 1

    @staticmethod
    def get_next_id() -> int:
        return Customer.counter

    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'
