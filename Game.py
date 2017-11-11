import random
import player  

def start_turn(player):
    def gain_devotion():
        x = input('Enter which devotion to gain: ')
        elements = [player.devotion1, player.devotion2]
        if x in elements:
            player.x = player.x + 1
            return player.x
        else:
            return gain_devotion()
            
def main():
    x = random.randrange(1, 3)
    if x == 1:
        start_turn('Player1')
    elif x == 2:
        start_turn('Player2')

main() 
