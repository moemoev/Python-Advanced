from animal import Animal
from lion import Lion
from tiger import Tiger
from cheetah import Cheetah
from worker import Worker
from keeper import Keeper
from caretaker import Caretaker
from vet import Vet

class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def space_left(self, obj: object):
        if isinstance(obj, Animal):
            return len(self.animals) < self.__animal_capacity
        elif isinstance(obj, Worker):
            return len(self.workers) < self.__workers_capacity

    def enough_budget(self, cost: int):

        return self.__budget >= cost

    def add_animal(self, animal: Animal, price: int):
        if not self.space_left(animal):

            return f"Not enough space for animal"

        if not self.enough_budget(price):

            return f"Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if not self.space_left(worker):
            return f"Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def get_worker(self, worker_name: str):
        for w in self.workers:
            if w.name == worker_name:

                return w

        return None


    def fire_worker(self, worker_name: str):
        worker = self.get_worker(worker_name)
        if not worker:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        cost = sum(w.salary for w in self.workers)

        if not self.enough_budget(cost):

            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= cost

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        cost = sum(a.money_for_care for a in self.animals)

        if not self.enough_budget(cost):
            return f"You have no budget to tend the animals. They are unhappy."

        self.__budget -= cost

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]

        lines = ''

        for animal, animal_group in {
            "Lions": lions,
            "Tigers": tigers,
            "Cheetahs": cheetahs,
        }.items():

            lines += f"----- {len(animal_group)} {animal}:\n" + '\n'.join(repr(a) for a in animal_group) + '\n'


        result = f"You have {len(self.animals)} animals\n" + f"{lines}"

        return result.strip()

    def workers_status(self):
        keepers = [w for w in self.workers if isinstance(w, Keeper)]
        caretakers = [w for w in self.workers if isinstance(w, Caretaker)]
        vets = [w for w in self.workers if isinstance(w, Vet)]

        lines = ''

        for worker, worker_group in {
            "Keepers": keepers,
            "Caretakers": caretakers,
            "Vets": vets,
        }.items():

            lines += f"----- {len(worker_group)} {worker}:\n" + '\n'.join(repr(w) for w in worker_group) + '\n'


        result = f"You have {len(self.workers)} workers\n" + f"{lines}"

        return result.strip()

zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
