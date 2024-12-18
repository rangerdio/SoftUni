from clients.regular_client import RegularClient
from clients.vip_client import VIPClient
from waiters.full_time_waiter import FullTimeWaiter
from waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    def __init__(self):
        self.waiters = []
        self.clients = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        pass

    def admit_client(self, client_type: str, client_name: str):
        pass

    def process_shifts(self, waiter_name: str):
        pass

    def process_client_order(self, client_name: str, order_amount: float):
        pass

    def apply_discount_to_client(self, client_name: str):
        pass

    def generate_report(self):
        pass
