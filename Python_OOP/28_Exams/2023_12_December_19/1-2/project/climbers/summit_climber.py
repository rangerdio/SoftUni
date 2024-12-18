from project.climbers.base_climber import BaseClimber

class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 150)

    def can_climb(self):
        pass

    def climb(self, peak):
        pass
