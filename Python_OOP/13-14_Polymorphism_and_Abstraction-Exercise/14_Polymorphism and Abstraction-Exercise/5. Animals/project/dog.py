from project.animal import Animal


class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.my_sound = 'Woof!'

    def make_sound(self):
        return self.my_sound

    @property
    def get_my_class_name(self):
        return self.__class__.__name__
