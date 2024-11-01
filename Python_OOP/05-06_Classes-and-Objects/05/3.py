class Circle:
    pi = 3.14

    def __init__(self, radius: float):
        self.radius = radius

    def set_radius(self, radius: float):
        self.radius = radius

    def get_area(self, pi=pi):
        return self.radius ** 2 * pi

    def get_circumference(self, pi=pi):
        return self.radius * 2 * pi


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
