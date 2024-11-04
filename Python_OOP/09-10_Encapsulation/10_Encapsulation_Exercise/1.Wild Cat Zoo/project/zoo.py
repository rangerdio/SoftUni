from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            # self.__animal_capacity -= 1

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__budget < price and self.__animal_capacity > len(self.animals):
            return 'Not enough budget'
        return 'Not enough space for animal'

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return 'Not enough space for worker'
        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name):
        w = [worker for worker in self.workers if worker.name == worker_name]
        if not w:
            return f'There is no {worker_name} in the zoo'
        self.workers.remove(w[0])
        return f'{w[0].name} fired successfully'

    def pay_workers(self):
        total_salary = sum([worker.salary for worker in self.workers])
        if self.__budget < total_salary:
            return f'You have no budget to pay your workers. They are unhappy'
        self.__budget -= total_salary
        return f'You payed your workers. They are happy. Budget left: {self.__budget}'

    def tend_animals(self):
        tending_price = sum([animal.money_for_care for animal in self.animals])
        if self.__budget < tending_price:
            return 'You have no budget to tend the animals. They are unhappy.'
        self.__budget -= tending_price
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions, tigers, cheetahs = 0, 0, 0
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions += 1
            elif animal.__class__.__name__ == 'Tiger':
                tigers += 1
            elif animal.__class__.__name__ == 'Cheetah':
                cheetahs += 1

        result = [f'You have {lions + tigers + cheetahs} animals', f'----- {lions} Lions:']
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                result.append(f'{animal.__repr__()}')
        result.append(f'----- {tigers} Tigers:')
        for animal in self.animals:
            if animal.__class__.__name__ == 'Tiger':
                result.append(f'{animal.__repr__()}')
        result.append(f'----- {cheetahs} Cheetahs:')
        for animal in self.animals:
            if animal.__class__.__name__ == 'Cheetah':
                result.append(f'{animal.__repr__()}')
        return '\n'.join(result)

    def workers_status(self):
        keepers, caretakers, vets = 0, 0, 0
        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers += 1
            elif worker.__class__.__name__ == 'Caretaker':
                caretakers += 1
            elif worker.__class__.__name__ == 'Vet':
                vets += 1

        result = [f'You have {keepers + caretakers + vets} workers', f'----- {keepers} Keepers:']
        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                result.append(f'{worker.__repr__()}')
        result.append(f'----- {caretakers} Caretakers:')
        for worker in self.workers:
            if worker.__class__.__name__ == 'Caretaker':
                result.append(f'{worker.__repr__()}')
        result.append(f'----- {vets} Vets:')
        for worker in self.workers:
            if worker.__class__.__name__ == 'Vet':
                result.append(f'{worker.__repr__()}')
        return '\n'.join(result)
