from clients.regular_client import RegularClient
from clients.vip_client import VIPClient
from waiters.full_time_waiter import FullTimeWaiter
from waiters.half_time_waiter import HalfTimeWaiter

class SphereRestaurantApp:
    def __init__(self):
        self.waiters = []
        self.clients = []

    def get_waiter_by_name(self, name: str):
        waiter = next((w for w in self.waiters if w.name == name), None)
        if not waiter:
            raise ValueError(f"No waiter found with the name {name}.")
        return waiter

    def get_client_by_name(self, name: str):
        client = next((c for c in self.clients if c.name == name), None)
        if not client:
            raise ValueError(f"No client found with the name {name}.")
        return client

    def create_waiter(self, waiter_type: str, name: str, hours_worked: int):
        if hours_worked <= 0:
            raise ValueError("Working hours must be positive!")
        if waiter_type == "FullTimeWaiter":
            return FullTimeWaiter(name, hours_worked)
        elif waiter_type == "HalfTimeWaiter":
            return HalfTimeWaiter(name, hours_worked)
        raise ValueError(f"{waiter_type} is not a recognized waiter type.")

    def create_client(self, client_type: str, name: str):
        if client_type == "RegularClient":
            return RegularClient(name)
        elif client_type == "VIPClient":
            return VIPClient(name)
        raise ValueError(f"{client_type} is not a recognized client type.")

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if any(w.name == waiter_name for w in self.waiters):
            raise ValueError(f"{waiter_name} is already on the staff.")
        waiter = self.create_waiter(waiter_type, waiter_name, hours_worked)
        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if any(c.name == client_name for c in self.clients):
            raise ValueError(f"{client_name} is already a client.")
        client = self.create_client(client_type, client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = self.get_waiter_by_name(waiter_name)
        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client = self.get_client_by_name(client_name)
        if order_amount <= 0:
            raise ValueError("Order amount must be positive!")
        points_earned = client.earning_points(order_amount)
        return f"{client_name} earned {points_earned} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = self.get_client_by_name(client_name)
        discount, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount}% discount. Remaining points {remaining_points}"

    def generate_report(self):
        total_earnings = sum(w.calculate_earnings() for w in self.waiters)
        total_client_points = sum(c.points for c in self.clients)
        clients_count = len(self.clients)

        report = [
            "$$ Monthly Report $$",
            f"Total Earnings: ${total_earnings:.2f}",
            f"Total Clients Unused Points: {total_client_points}",
            f"Total Clients Count: {clients_count}",
            "** Waiter Details **"
        ]

        sorted_waiters = sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True)
        for waiter in sorted_waiters:
            report.append(str(waiter))

        return "\n".join(report)
