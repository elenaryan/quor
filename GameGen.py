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
        if turn % 2 == 0:
            flip = random.randint(0,1)
            if flip == 0:
                if walls1 > 0:
                    wplace = 0
                    while wplace == 0:
                        direct = ['v', 'h']
                        ind1 = random.randint(0,8)
                        ind2 = random.randint(0,8)
                        dirw = direct[random.randint(0,1)]
                        try:
                            game.addWall((ind1, ind2), dirw)#to place the wall
                            if (not(game.canStillWin()) or not(game.canStillWin2())):
                                print "IT WORKS"
                                game.remWall((ind1, ind2), dirw)
                            else:
                                walls1 = walls1 - 1
                                wplace = 1
                        except:
                            print str(ind1) + " " + str(ind2) + " " + dirw
                            game.remWall((ind1, ind2), dirw)
                            #pass
                    else:
                        pass
                    '''
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
                    '''        
                            

                           
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

        else:
            flip = random.randint(0,1)
            if flip == 0:
                if walls2 > 0:
                    wplace = 0
                    while wplace == 0:
                        direct = ['v', 'h']
                        ind1 = random.randint(0,8)
                        ind2 = random.randint(0,8)
                        dirw = direct[random.randint(0,1)]
                        try:
                            game.addWall((ind1, ind2), dirw)#to place the wall
                            if (not(game.canStillWin()) or not(game.canStillWin2())):
                                print "IT WORKS"
                                game.remWall((ind1, ind2), dirw)
                            else:
                                walls2 = walls2 - 1
                                wplace = 1
                        except:
                            print str(ind1) + " " + str(ind2) + " " + dirw
                            game.remWall((ind1, ind2), dirw)
                            #pass
                    else:
                        pass
                    '''
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
                    '''        
                            

                           
            else:
                poss1 = [pos2[0]+1, pos2[0]-1]
                poss2 = [pos2[1]+1, pos2[1]-1]
                flip = random.randint(0,1)
                chosen = 0
                while chosen == 0:
                    flip = random.randint(0,1)
                    if flip == 0:
                        flip = random.randint(0,1)
                        mv = poss1[flip]
                        if mv >=0 and mv <=8 and (mv, pos2[1]) != pos1:
                            
                            pos2 = mv,pos2[1]
                            chosen = 1
                    else:
                        flip = random.randint(0,1)
                        mv = poss2[flip]
                        if mv >=0 and mv <=8 and (pos2[0], mv) != pos1:
                            pos2 = pos2[0],mv
                            chosen = 1
            
            #pass
        




        
        moves.append((pos1, turn))
        turn = turn + 1 #just making sure we keep alternating bt turns
    #print "We Have Reached the end! \n"
    if pos1[1] == 0:
        print "Player 1 wins! "
    else:
        print "Player 2 wins! "
    print "Total turns: "+str(turn-1)
    print pos1
    print pos2
    print "Player 1 has "+str(walls1)+" remaining"
    print "Player 2 has "+str(walls2)+" remaining"
    #print moves
    print len(game.getWalls())
    #At the end, depending who wins, loop through the array of tuples and create a new array
    #where the winning teams moves are tagged with win or loss


if __name__ == "__main__":
    main()


    
