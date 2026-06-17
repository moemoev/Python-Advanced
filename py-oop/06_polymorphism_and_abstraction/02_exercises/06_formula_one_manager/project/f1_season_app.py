from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam


class F1SeasonApp:
    VALID_TEAMS = ['Red Bull', 'Mercedes']

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name not in self.VALID_TEAMS:
            raise ValueError("Invalid team name!")

        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
        else:
            self.mercedes_team = MercedesTeam(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not all(False for team in self.__dict__.values() if team is None):
            return "Not all teams have registered for the season."

        rb_rev = f"{self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}"
        mer_rev = f"{self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}"

        positions = {
            "Red Bull": red_bull_pos,
            "Mercedes": mercedes_pos
        }

        return f"Red Bull: {rb_rev}. Mercedes: {mer_rev}. {min(positions, key=positions.get)} is ahead at the {race_name} race."