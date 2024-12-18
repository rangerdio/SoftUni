from project.peaks.base_peak import BasePeak
from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 200)

    def can_climb(self):
        pass

    def climb(self, peak: BasePeak):
        pass