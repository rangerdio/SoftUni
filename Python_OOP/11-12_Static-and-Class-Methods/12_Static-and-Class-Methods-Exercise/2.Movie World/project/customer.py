from project.dvd import DVD


class Customer:
    def __init__(self, name: str, age: int, _id: int) -> None:
        self.name = name
        self.age = age
        self.id = _id
        self.rented_dvds: list[DVD] = []

    def __repr__(self):
        return (f"{self.id}: {self.name} of age {self.age} "
                f"has {len(self.rented_dvds)} rented DVD's ({', '.join([dvd.name for dvd in self.rented_dvds])})")


# cust1 = Customer('koko', 18, 1234124)
# cust2 = Customer('boko', 14, 1234524)
# gundi = Dvd('Gundi')
# smurfs = Dvd('The Smurfs')
# cust1.rented_dvds.append(gundi)
# cust1.rented_dvds.append(smurfs)
#
# print(cust1)
# print(cust2)
