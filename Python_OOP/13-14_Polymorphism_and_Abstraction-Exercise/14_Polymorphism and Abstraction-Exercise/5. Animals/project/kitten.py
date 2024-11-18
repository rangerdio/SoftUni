from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Female")
        self.my_sound = 'Meow'

    def make_sound(self):
        return self.my_sound

    @property
    def get_my_class_name(self):
        return self.__class__.__name__
