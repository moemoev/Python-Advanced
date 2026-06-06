class Vet:
    animals = []
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def get_animal_space_in_clinic(self):
        space = Vet.space - len(Vet.animals)

        return space

    def info(self):
        number_animals = len(self.animals)
        space_left_in_clinic = self.get_animal_space_in_clinic()

        return f"{self.name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"

    def register_animal(self, animal_name: str):
        if self.get_animal_space_in_clinic() == 0:

            return f"Not enough space"

        Vet.animals.append(animal_name)
        self.animals.append(animal_name)

        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name: str):

        if animal_name not in self.animals:

            return f"{animal_name} not in the clinic"

        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)

        return f"{animal_name} unregistered successfully"

        

peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
