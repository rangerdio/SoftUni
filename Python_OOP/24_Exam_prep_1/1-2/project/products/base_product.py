from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, model: str, price: float, material: str, sub_type: str):
        if len(model.strip()) < 3:
            raise ValueError("Product model must be at least 3 chars long!")
        if price <= 0.0:
            raise ValueError("Product price must be greater than zero!")
        self.model = model
        self.price = price
        self.material = material
        self.sub_type = sub_type

    @abstractmethod
    def discount(self):
        pass
