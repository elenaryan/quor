'''
    This is going to be a quoridor valid game generator writted in Python
    It will write out valid python games that are random but still legal.
    At its core it shall use the quoridor graph to determine which paths are legal
    and available.  That being said, it's finna be pretty random

    Elena Ryan | CISC Researching 4/2018
    

'''

import QBoard as q


#gotta decide how we wanna structure this bad boy
#at this point will create a text file of valid games
#initialize total num walls & first positions

#How do I test to see if a wall is valid without actually placing it??
#Need to add a removewall function to QBoard I think

def generategame():
    1walls = 10
    2walls = 10
    1pos   = 4,8
    2pos   = 4,0
    turn   = 0
    game   = ""


    game = q.QBoard()
    game.placePlayer(1pos)
    game.placePlayer2(2pos)
    
    while 1pos[1] != 0 and 2pos[1] !=8:
        #this is the while loop where the game is created
        if turn % 2 == 0:
            #this will be a black turn
            # we get the option between either laying a wall
            # or advancing the piece but we need to stay such that there
            #aren't any wall violations and try to advance

        else:
            #this will be a white turn
        
    
    
