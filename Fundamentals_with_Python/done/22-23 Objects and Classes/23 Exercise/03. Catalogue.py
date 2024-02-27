class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name


    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [element for element in Catalogue.products if element[0] == first_letter]

    def __repr__(self):
        new_list = sorted(Catalogue.products)
        new_list.insert(0, f"Items in the {self.name} catalogue:")
        return "\n".join(new_list)


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
