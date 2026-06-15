class Subscription:
    ID = 1

    def __init__(self, date: str, customer_id: str, trainer_id: str, exercise_id: int):
        self.id = Subscription.ID
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id

        Subscription.ID = Subscription.get_next_id()

    def __repr__(self):
        result = f"Subscription <{self.id}> on {self.date}"
        return result

    @staticmethod
    def get_next_id():
        return Subscription.ID