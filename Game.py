import random
import player  

def gain_devotion(player):
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
        y = gain_devotion('Player1')
    elif x == 2:
        y = gain_devotion('Player2')
    print(y)    

main() 
