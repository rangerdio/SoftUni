from project.trainer import Trainer
from project.customer import Customer
from project.equipment import Equipment
from project.subscription import Subscription
from project.exercise_plan import ExercisePlan


class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer) if customer not in self.customers else None

    def add_trainer(self, trainer: Trainer):
        self.trainers.append(trainer) if trainer not in self.trainers else None

    def add_equipment(self, equipment: Equipment):
        self.equipment.append(equipment) if equipment not in self.equipment else None

    def add_plan(self, plan: ExercisePlan):
        self.plans.append(plan) if plan not in self.plans else None

    def add_subscription(self, subscription: Subscription):
        self.subscriptions.append(subscription) if subscription not in self.subscriptions else None

    def subscription_info(self, subscription_id: int):
        subscription = [sub for sub in self.subscriptions if sub.id == subscription_id][0]
        customer_id, trainer_id = subscription.trainer_id, subscription.trainer_id
        customer = [cust for cust in self.customers if cust.id == customer_id][0]
        trainer = [tr for tr in self.trainers if tr.id == trainer_id][0]
        plan = [pl for pl in self.plans if pl.trainer_id == trainer_id][0]
        equipment_id = plan.equipment_id
        equipment = [eq for eq in self.equipment if eq.id == equipment_id][0]
        return f'{repr(subscription)}\n{repr(customer)}\n{repr(trainer)}\n{repr(equipment)}\n{repr(plan)}'
