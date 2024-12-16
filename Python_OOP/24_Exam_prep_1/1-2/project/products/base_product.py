from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, model: str, price: float, material: str, sub_type: str):
        self.model = model
        self.price = price
        self.material = material
        self.sub_type = sub_type

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value: str):
        if len(value.strip()) < 3:
            raise ValueError("Product model must be at least 3 chars long!")
        self._model = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0.0:
            raise ValueError("Product price must be greater than zero!")
        self._price = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value: str):
        if not value.strip():
            raise ValueError("Product material cannot be empty!")
        self._material = value

    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value: str):
        if not value.strip():
            raise ValueError("Product sub-type cannot be empty!")
        self._sub_type = value

    @abstractmethod
    def discount(self):
        pass
