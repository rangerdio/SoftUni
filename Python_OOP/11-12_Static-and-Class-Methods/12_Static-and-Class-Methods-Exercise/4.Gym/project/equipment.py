class Equipment:
    equipment_id_counter = 1

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = Equipment.equipment_id_counter
        Equipment.equipment_id_counter += 1

    @staticmethod
    def get_next_id() -> int:
        return Equipment.equipment_id_counter

    def __repr__(self):
        return f'Equipment <{self.id}> {self.name}'
