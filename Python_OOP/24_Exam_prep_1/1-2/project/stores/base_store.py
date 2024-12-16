from abc import ABC, abstractmethod

class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int):
        if not name.strip():
            raise ValueError("Store name cannot be empty!")
        if len(location.strip()) != 3 or " " in location:
            raise ValueError("Store location must be 3 chars long!")
        if capacity < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products = []

    def get_estimated_profit(self):
        total_price = sum(product.price for product in self.products)
        profit = total_price * 0.1
        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"

    @property
    @abstractmethod
    def store_type(self):
        pass

    @abstractmethod
    def store_stats(self):
        pass
