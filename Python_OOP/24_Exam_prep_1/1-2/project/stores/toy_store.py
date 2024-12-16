from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=100)

    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        available_products = {}
        for product in self.products:
            if product.model not in available_products:
                available_products[product.model] = []
            available_products[product.model].append(product.price)

        details = []
        for model, prices in sorted(available_products.items()):
            num_products = len(prices)
            avg_price = sum(prices) / num_products
            details.append(f"{model}: {num_products}pcs, average price: {avg_price:.2f}")

        stats = (
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
            f"{self.get_estimated_profit()}\n"
            f"**Toys for sale:"
        )

        if details:
            stats += "\n" + "\n".join(details)
        return stats
