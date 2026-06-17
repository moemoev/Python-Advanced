from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    REVENUE = {
        'Oracle': {
            1: 1.5 * 10 ** 6,
            2: 8 * 10 ** 5
        },
        'Honda': {
            8: 2 * 10 ** 4,
            10: 10 ** 4
        }
    }
    EXPENSES = 2.5 * 10 ** 5

    def __init__(self, budget):
        super().__init__(budget)
