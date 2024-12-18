from .base_client import BaseClient

class RegularClient(BaseClient):
    def __init__(self, name: str):
        super().__init__(name, "Regular")

    def earning_points(self, order_amount: float):
        if order_amount <= 0:
            raise ValueError("Order amount must be positive!")
        points_earned = int(order_amount // 10)
        self.points += points_earned
        return points_earned