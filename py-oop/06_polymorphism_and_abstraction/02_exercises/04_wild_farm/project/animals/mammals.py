from project.animals.animal import Mammal
from project.food import Food, Meat, Vegetable, Fruit


class Mouse(Mammal):
    ALLOWED_FOOD = (Vegetable, Fruit)
    WEIGHT_GAIN = 0.1

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if not isinstance(food, (Vegetable, Fruit)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += 0.1 * food.quantity


class Dog(Mammal):
    ALLOWED_FOOD = Meat
    WEIGHT_GAIN = 0.4

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += 0.4 * food.quantity


class Cat(Mammal):
    ALLOWED_FOOD = Meat
    WEIGHT_GAIN = 0.3

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if not isinstance(food, (Vegetable, Meat)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += 0.3 * food.quantity


class Tiger(Mammal):
    ALLOWED_FOOD = Meat
    WEIGHT_GAIN = 1

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += 1 * food.quantity


