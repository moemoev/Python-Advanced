from project.animals.animal import Bird
from project.food import Food, Meat


class Owl(Bird):
    ALLOWED_FOOD = Meat
    WEIGHT_GAIN = 0.25
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    WEIGHT_GAIN = 0.35

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

