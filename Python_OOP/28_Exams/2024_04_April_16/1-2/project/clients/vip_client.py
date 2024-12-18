from .base_client import BaseClient


class VIPClient(BaseClient):
    def __init__(self, name: str):
        super().__init__(name, "VIP")

    def earning_points(self, order_amount: float):
        pass

    def apply_discount(self):
        pass
