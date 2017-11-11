class Hero(object):
    def __init__(self, name):
        self.name = name
        self.health = 30
        def get_devotion1():
            x = input('Enter your primary devotion ' + self.name + ': ')
            elements = ['earth', 'fire', 'water', 'wind', 'lightning']
            if x in elements:
                return x
            else:
                return get_devotion1()
        def get_devotion2():
            y = input('Enter your second devotion ' + self.name + ': ')
            elements = ['earth', 'fire', 'water', 'wind', 'lightning']
            if y in elements:
                return y
            elif y == 'none':
                return None
            else:
                return get_devotion2()
            
        self.devotion1 = get_devotion1()
        self.devotion2 = get_devotion2()
        self.earth = 0
        self.wind = 0
        self.fire = 0
        self.water = 0
        self.lightning = 0

Player1 = Hero('Player1')
Player2 = Hero('Player2')

def test():
    print(Player1.name)
    print(Player1.health)
    print(Player1.devotion1)
    print(Player1.devotion2)
