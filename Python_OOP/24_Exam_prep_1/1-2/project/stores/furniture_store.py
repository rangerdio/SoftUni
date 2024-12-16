from project.stores.base_store import BaseStore

class FurnitureStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=50)

    @property
    def store_type(self):
        return "FurnitureStore"

    def store_stats(self):
        product_details = {}
        for product in self.products:
            if product.model not in product_details:
                product_details[product.model] = []
            product_details[product.model].append(product.price)

        stats = "\n".join(
            f"{model}: {len(prices)}pcs, average price: {sum(prices) / len(prices):.2f}"
            for model, prices in sorted(product_details.items())
        )
        return (
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
            f"{self.get_estimated_profit()}\n"
            f"**Furniture for sale:\n{stats}"
        )
