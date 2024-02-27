class Inventory:

    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        items = []

    def add_item(self, item: str):
        pass

    def get_capacity(self):
        pass

    def __repr__(self):
        pass


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
