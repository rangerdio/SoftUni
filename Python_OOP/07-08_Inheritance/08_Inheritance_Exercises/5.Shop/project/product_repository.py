from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name):
        p = self.find(product_name)
        if p:
            self.products.remove(p)

    def __repr__(self):
        result = []
        for p in self.products:
            result.append(f'{p.name}: {p.quantity}')
        return '\n'.join(result)
