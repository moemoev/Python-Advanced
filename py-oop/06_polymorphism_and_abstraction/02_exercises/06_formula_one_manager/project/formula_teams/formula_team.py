from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    REVENUE = {}
    EXPENSES = 0

    @abstractmethod
    def __init__(self, budget: int):
        self.budget = self.validate_formula_budget(budget)

    @staticmethod
    def validate_formula_budget(budget):
        if budget < 10 ** 6:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        return budget

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        #TODO: REWORK DUDE
        for sponsor, rev in self.REVENUE.items():
            keys = [x for x in rev.keys() if x >= race_pos]
            if not keys:
                continue

            key = min(keys)
            revenue += rev[key]

        revenue -= self.EXPENSES

        self.budget += revenue

        return f"The revenue after the race is {int(revenue)}$. Current budget {int(self.budget)}$"
