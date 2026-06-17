from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    REVENUE = {
        'Petronas': {
            1: 10 ** 6,
            3: 5 * 10 ** 5
        },
        'TeamViewer': {
            5: 10 ** 5,
            7: 5 * 10 ** 4
        }
    }
    EXPENSES = 2 * 10 ** 5

    def __init__(self, budget):
        super().__init__(budget)
