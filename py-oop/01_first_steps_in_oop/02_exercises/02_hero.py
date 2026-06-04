class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        if not self.health - damage <= 0:
            self.health -= damage
            return
        self.health = 0
        return f"{self.name} was defeated"

    def heal(self, amount: int):
        self.health += amount


hero = Hero('Peter', 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))


'''
TASK:
Create a class called Hero. Upon initialization, it should receive a name (string) and health (number). Create two 
 additional methods:
defend(damage) - reduce the given damage from the hero's health:
if the health become 0 or less, set it to 0 and return "{name} was defeated"
heal(amount) - increase the health of the hero with the given amount
'''