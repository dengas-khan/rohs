class minion(object):
    def __init__(self, name, attack, health, race, earth, wind, fire, water, lightning):
        self.name = name
        self.attack = attack
        self.health = health
        self.race = race
        self.earth = earth
        self.wind = wind
        self.fire = fire
        self.water = water
        self.lightning = lightning
        self.battlecry = False
        self.deathrattle = False

Frostling = minion('Frostling', 1, 1, 'elemental', 0, 0, 0, 1, 0)
print(Frostling.name)
print(Frostling.attack)
print(Frostling.health)
print(Frostling.race)
print(Frostling.earth)
print(Frostling.water)

