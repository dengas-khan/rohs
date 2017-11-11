import random
import player  

def start_turn(player):
    def gain_devotion():
        x = input('Enter which devotion to gain: ')
        elements = ['earth', 'fire', 'water', 'wind', 'lightning']
        try:
            x in elements
            return x
        except:
            return gain_devotion()
        y = gain_devotion()
        player.y = player.y + 1
        print(player.y)

def main():
    x = random.randrange(1, 3)
    if x == 1:
        start_turn('Player1')
    elif x == 2:
        start_turn('Player2')

main() 
