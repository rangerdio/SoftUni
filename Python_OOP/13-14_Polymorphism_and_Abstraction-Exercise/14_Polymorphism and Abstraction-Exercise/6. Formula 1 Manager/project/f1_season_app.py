from typing import Union

from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team: Union[RedBullTeam, None] = None
        self.mercedes_team: Union[MercedesTeam, None] = None

    def register_team_for_season(self, team_name: str, budget: int) -> str:
        if team_name == 'Red Bull':
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == 'Mercedes':
            self.mercedes_team = MercedesTeam(budget)
        else:
            raise ValueError('Invalid team name!')
        return f'{team_name} has joined the new F1 season.'

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.mercedes_team or not self.red_bull_team:
            raise Exception('Not all teams have registered for the season.')
        faster = "Red Bull" if mercedes_pos > red_bull_pos else "Mercedes"
        return (f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. "
                f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. "
                f"{faster} is ahead at the {race_name} race.")
