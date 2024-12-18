from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak

class SummitQuestManagerApp:
    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        pass

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        pass

    def check_gear(self, climber_name: str, peak_name: str, gear: list):
        pass

    def perform_climbing(self, climber_name: str, peak_name: str):
        pass

    def get_statistics(self):
        pass
