class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self, radius):
        return 2 * Circle.__pi * radius

    def calculate_area(self, radius):
        return Circle.__pi ** radius

    def calculate_area_of_sector(self, angle):
        pass

