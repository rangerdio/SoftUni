class Trainer:
    trainer_id_counter = 1

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = Trainer.trainer_id_counter
        Trainer.trainer_id_counter += 1

    @staticmethod
    def get_next_id() -> int:
        return Trainer.trainer_id_counter

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
