from .base_client import BaseClient


class RegularClient(BaseClient):
    def __init__(self, name: str):
        super().__init__(name, "Regular")

    def earning_points(self, order_amount: float):
        pass

    def apply_discount(self):
        pass
