'''
    This is going to be a quoridor valid game generator writted in Python
    It will write out valid python games that are random but still legal.
    At its core it shall use the quoridor graph to determine which paths are legal
    and available.  That being said, it's finna be pretty random

    Elena Ryan | CISC Researching 4/2018
    

'''

import QBoard as q
import random


#gotta decide how we wanna structure this bad boy
#at this point will create a text file of valid games
#initialize total num walls & first positions

#How do I test to see if a wall is valid without actually placing it??
#Need to add a removewall function to QBoard I think
#seems as though I have to save the full state at any given mood -
#take a snapshot of board state with a tuple



def generategame():
    1walls = 10
    2walls = 10
    1pos   = 4,8
    2pos   = 4,0
    turn   = 0
    game   = ""
    chosen = 0 #basically a flag to make sure choices fall within range

    game = q.QBoard()
    game.placePlayer(1pos)
    game.placePlayer2(2pos)
    
    while 1pos[1] != 0 and 2pos[1] !=8:
        #this is the while loop where the game is created
        if turn % 2 == 0:
            flip = randint(0,1)
            if flip == 0:
                if 1walls > 0:
                    wplace = 0
                    while wplace == 0:
                        holdwalls = game.getWalls
                        direct = ['v', 'h']
                        ind1 = randint(0,8)
                        ind2 = randint(0,8)
                        dirw = direct[randint(0,1)]
                        try game.addWall((ind1, ind2), dirw)#to place the wall
                        except:
                            pass
                        else:
                            #check and see if both players can still win
                            
                            

                            #successfully placed the wall now gotta make sure it doesn't block anyone
                    #throws an exception if we try to place a wall over another wall
                    #so just loop a random wall placement until it works
                    #ALSO must make sure that with each valid wall placement, both players can still win
                #place a wall
            else:
                poss1 = [1pos[0]+1, 1pos[0]-1]
                poss2 = [1pos[1]+1, 1pos[1]-1]
                flip = randint(0,1)
                chosen = 0
                while chosen == 0:
                    flip = randint(0,1)
                    if flip == 0:
                        flip = randint(0,1)
                        mv = poss1[flip]
                        if mv >=0 and mv <=8 and (mv, 1pos[1]) != 2pos:
                            
                            1pos = mv,1pos[1]
                            chosen = 1
                    else:
                        flip = randint(0,1)
                        mv = poss2[flip]
                        if mv >=0 and mv <=8 and (1pos[0], mv) != 2pos:
                            1pos = 1pos[0],mv
                            chosen = 1
                #randomly move the player
                #advance the player
            #this will be a black turn
            # we get the option between either laying a wall
            # or advancing the piece but we need to stay such that there
            #aren't any wall violations and try to advance

        else:
            #this will be a white turn
        
    
    #At the end, depending who wins, loop through the array of tuples and create a new array
    #where the winning teams moves are tagged with win or loss 
