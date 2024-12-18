from .base_client import BaseClient

class VIPClient(BaseClient):
    def __init__(self, name: str):
        super().__init__(name, "VIP")

    def earning_points(self, order_amount: float):
        if order_amount <= 0:
            raise ValueError("Order amount must be positive!")
        points_earned = int(order_amount // 5)
        self.points += points_earned
        return points_earned
