class Equipment:
    ID = 1

    def __init__(self, name: str):
        self.id = Equipment.ID
        self.name = name

        Equipment.ID = Equipment.get_next_id()

    @staticmethod
    def get_next_id():
        return Equipment.ID

    def __repr__(self):
        result = f"Equipment <{self.id}> {self.name}"
        return result