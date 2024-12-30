from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    def __init__(self, name: str, phone_number: str):
        super().__init__(name, phone_number)

    def update_discount(self):
        if self.total_orders >= 1:
            self.discount = 5.0
        else:
            self.discount = 0.0

    def client_details(self):
        return super().client_details()