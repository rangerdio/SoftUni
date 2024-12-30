from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    def __init__(self):
        self.income = 0.0
        self.plants = []
        self.clients = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type == "Flower":
            plant = Flower(plant_name, plant_price, plant_water_needed, plant_extra_data)
        elif plant_type == "LeafPlant":
            plant = LeafPlant(plant_name, plant_price, plant_water_needed, plant_extra_data)
        else:
            raise ValueError("Unknown plant type!")
        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if any(client.phone_number == client_phone_number for client in self.clients):
            raise ValueError("This phone number has been used!")
        if client_type == "RegularClient":
            client = RegularClient(client_name, client_phone_number)
        elif client_type == "BusinessClient":
            client = BusinessClient(client_name, client_phone_number)
        else:
            raise ValueError("Unknown client type!")
        self.clients.append(client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if not client:
            raise ValueError("Client not found!")
        available_plants = [p for p in self.plants if p.name.lower() == plant_name.lower()]
        if not available_plants:
            raise ValueError("Plants not found!")
        if len(available_plants) < plant_quantity:
            return "Not enough plant quantity."
        total_price = sum(p.price for p in available_plants[:plant_quantity])
        total_price *= (1 - client.discount / 100)
        self.income += total_price
        for _ in range(plant_quantity):
            self.plants.remove(next(p for p in self.plants if p.name.lower() == plant_name.lower()))
        client.update_total_orders()
        client.update_discount()
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {total_price:.2f}"

    def remove_plant(self, plant_name: str):
        for i, plant in enumerate(self.plants):
            if plant.name == plant_name:
                removed_plant = self.plants.pop(i)
                return f"Removed {removed_plant.plant_details()}"
        return "No such plant name."

    def remove_clients(self):
        removed_clients = [c for c in self.clients if c.total_orders == 0]
        self.clients = [c for c in self.clients if c.total_orders > 0]
        return f"{len(removed_clients)} client/s removed."

    def shop_report(self):
        report = [
            f"~Flower Shop Report~",
            f"Income: {self.income:.2f}",
            f"Count of orders: {sum(c.total_orders for c in self.clients)}",
            f"~~Unsold plants: {len(self.plants)}~~"
        ]
        plant_counts = {}
        for plant in self.plants:
            plant_counts[plant.name] = plant_counts.get(plant.name, 0) + 1
        for plant_name, count in sorted(plant_counts.items(), key=lambda x: (-x[1], x[0])):
            report.append(f"{plant_name}: {count}")
        report.append(f"~~Clients number: {len(self.clients)}~~")
        for client in sorted(self.clients, key=lambda x: (-x.total_orders, x.phone_number)):
            report.append(client.client_details())
        return "\n".join(report)
