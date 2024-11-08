from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity() -> int:
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers and len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if dvd not in self.dvds and len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        # customer = [cust for cust in self.customers if customer_id == cust.id][0]
        # dvd = [d for d in self.dvds if dvd_id == d.id][0]
        customer = self.get_customer(customer_id)
        dvd = self.get_dvd(dvd_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        # customer = [cust for cust in self.customers if customer_id == cust.id][0]
        # dvd = [d for d in self.dvds if dvd_id == d.id][0]
        customer = self.get_customer(customer_id)
        dvd = self.get_dvd(dvd_id)
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def get_customer(self, customer_id: int) -> Customer:
        return [cust for cust in self.customers if customer_id == cust.id][0]

    def get_dvd(self, dvd_id: int) -> DVD:
        return [d for d in self.dvds if dvd_id == d.id][0]

    def __repr__(self):
        result = []
        result.extend(repr(cust) for cust in self.customers)
        result.extend(repr(dvd) for dvd in self.dvds)
        return '\n'.join(result)
