from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'Male')
        self.my_sound = 'Hiss'

    def make_sound(self):
        return self.my_sound

    @property
    def get_my_class_name(self):
        return self.__class__.__name__
