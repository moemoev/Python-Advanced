from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription

class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_obj(self, obj: object, obj_ll: list):
        if obj not in obj_ll:
            obj_ll.append(obj)

    def add_customer(self, customer: Customer):
        self.add_obj(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.add_obj(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.add_obj(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.add_obj(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.add_obj(subscription, self.subscriptions)

    def get_obj_by_id(self, obj_id: int, obj_ll: list):
        for obj in obj_ll:
            if obj.id == obj_id:
                return obj

    def subscription_info(self, subscription_id: int):
        subscription = self.get_obj_by_id(subscription_id, self.subscriptions)
        customer = self.get_obj_by_id(subscription.customer_id, self.customers)
        trainer = self.get_obj_by_id(subscription.trainer_id, self.trainers)
        plan = self.get_obj_by_id(subscription.exercise_id, self.plans)
        equipment = self.get_obj_by_id(plan.equipment_id, self.equipment)

        result = f"{str(subscription)}\n"
        result += f"{str(customer)}\n"
        result += f"{str(trainer)}\n"
        result += f"{str(equipment)}\n"
        result += f"{str(plan)}"

        return result