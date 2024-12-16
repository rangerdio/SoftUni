from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type == "Chair":
            product = Chair(model, price)
        elif product_type == "HobbyHorse":
            product = HobbyHorse(model, price)
        else:
            raise Exception("Invalid product type!")
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type == "FurnitureStore":
            store = FurnitureStore(name, location)
        elif store_type == "ToyStore":
            store = ToyStore(name, location)
        else:
            raise Exception(f"{store_type} is an invalid type of store!")
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store, *products):
        if len(products) > store.capacity:
            return f"Store {store.name} has no capacity for this purchase."

        # Filter valid products based on the store's type
        valid_products = [p for p in products if store.store_type.rstrip("Store") in p.sub_type]

        # If no valid products match, return the appropriate message
        if not valid_products:
            return "Products do not match in type. Nothing sold."

        # Otherwise, process the valid products
        for product in valid_products:
            store.products.append(product)
            self.products.remove(product)

        store.capacity -= len(valid_products)
        self.income += sum(product.price for product in valid_products)
        return f"Store {store.name} successfully purchased {len(valid_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            return "There is no store registered under this name!"
        return store.store_stats()

    def discount_products(self, model: str):
        count = 0
        for product in self.products:
            if product.model == model:
                product.discount()
                count += 1
        return f"Discount applied to {count} products with model: {model}"

    def statistics(self):
        unsold_product_counts = {}
        for product in self.products:
            if product.model not in unsold_product_counts:
                unsold_product_counts[product.model] = 0
            unsold_product_counts[product.model] += 1

        unsold_products_details = "\n".join(
            f"{model}: {count}" for model, count in sorted(unsold_product_counts.items())
        )

        total_unsold_price = sum(product.price for product in self.products)
        partner_store_names = "\n".join(sorted(store.name for store in self.stores))

        return (
            f"Factory: {self.name}\n"
            f"Income: {self.income:.2f}\n"
            f"***Products Statistics***\n"
            f"Unsold Products: {len(self.products)}. Total net price: {total_unsold_price:.2f}\n"
            f"{unsold_products_details}\n"
            f"***Partner Stores: {len(self.stores)}***\n"
            f"{partner_store_names}"
        )
