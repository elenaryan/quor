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



def main():
    print "Velkommen"
    generategame()

def generategame():
    walls1 = 10
    walls2 = 10
    pos1   = 4,8
    pos2   = 4,0
    turn   = 0
    game   = ""
    chosen = 0 #basically a flag to make sure choices fall within range
    moves = []
    game = q.QBoard()
    game.placePlayer(pos1)
    game.placePlayer2(pos2)
    
    while pos1[1] != 0 and pos2[1] !=8:
        #this is the while loop where the game is created
        if turn % 2 == 0:
            flip = random.randint(0,1)
            if flip == 0:
                if walls1 > 0:
                    wplace = 0
                    while wplace == 0:
                        holdwalls = game.getWalls
                        direct = ['v', 'h']
                        ind1 = random.randint(0,8)
                        ind2 = random.randint(0,8)
                        dirw = direct[random.randint(0,1)]
                        try:
                            game.addWall((ind1, ind2), dirw)#to place the wall
                        except:
                            pass
                        else:
                            if (not(game.canStillWin()) or not(game.canStillWin2())):
                                game.setWalls(holdwalls)
                            else:
                                walls1 = walls1 - 1
                                wplace = 1
                            #check and see if both players can still win

                    else:
                        pass
                            
                            

                            #successfully placed the wall now gotta make sure it doesn't block anyone
                    #throws an exception if we try to place a wall over another wall
                    #so just loop a random wall placement until it works
                    #ALSO must make sure that with each valid wall placement, both players can still win
                #place a wall
            else:
                poss1 = [pos1[0]+1, pos1[0]-1]
                poss2 = [pos1[1]+1, pos1[1]-1]
                flip = random.randint(0,1)
                chosen = 0
                while chosen == 0:
                    flip = random.randint(0,1)
                    if flip == 0:
                        flip = random.randint(0,1)
                        mv = poss1[flip]
                        if mv >=0 and mv <=8 and (mv, pos1[1]) != pos2:
                            
                            pos1 = mv,pos1[1]
                            chosen = 1
                    else:
                        flip = random.randint(0,1)
                        mv = poss2[flip]
                        if mv >=0 and mv <=8 and (pos1[0], mv) != pos2:
                            pos1 = pos1[0],mv
                            chosen = 1
                #randomly move the player
                #advance the player
            #this will be a black turn
            # we get the option between either laying a wall
            # or advancing the piece but we need to stay such that there
            #aren't any wall violations and try to advance

        else:
            pass
        
            #this will be a white turn
        moves.append((pos1, turn))
        turn = turn + 1 #just making sure we keep alternating bt turns
    print "We Have Reached the end! \n"
    print pos1
    print pos2
    print walls1
    print walls2
    print moves
    #At the end, depending who wins, loop through the array of tuples and create a new array
    #where the winning teams moves are tagged with win or loss


if __name__ == "__main__":
    main()


    
