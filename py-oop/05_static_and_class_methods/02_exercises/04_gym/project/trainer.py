class Trainer:
    ID = 1

    def __init__(self, name: str):
        self.id = Trainer.ID
        self.name = name

        Trainer.ID = Trainer.get_next_id()

    @staticmethod
    def get_next_id():
        return Trainer.ID

    def __repr__(self):
        result = f"Trainer <{self.id}> {self.name}"
        return result