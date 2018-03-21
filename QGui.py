# code derived from checkerboard code at http://www.cs.bc.edu/~straubin/cs101-2014/checkerboard.py , though with many modifications.

'''
        Code altered 3/2018 as part of quoridor implementation
        Currently connected to the quoridor.py driver which basically just
        needs to translate our chosen acceptable formatting into something that
        the already built graph and board implementations can understand

        In its original form this program
                A. only supported a single player position
                B. located the shorted possible path between the origin and the end
        What will be changed upon its completion
                A. Will support two players whose moves are updated in succession
                B. Will determine IF there exists a shortest path before accepting any wall placements
                        i. This can be fairly easily accomplished by utilization of QBoard and Qgraph




'''





from Tkinter import *
import random
import QBoard as qu

def draw_quoridor(can, walls=[], path=[], player=(4,8), player2=(4, 0)):
	side = 9
	smallw=50
	smallh=50
	gap=8
	for i in range(side):
		for j in range(side):
			xcorn=j*smallw+j*gap
			ycorn=i*smallh+i*gap
			fillcolor='darkgray'
			can.create_rectangle(xcorn,ycorn,xcorn+smallw,ycorn+smallh,fill=fillcolor)
	draw_mult_walls(can, walls)
	#draw_path(can, path)
	draw_player(can, player)
	draw_player2(can, player2)


def draw_path(can, path):
	for i in range(0, len(path)-1):
		(xstart, ystart) = getMidPoint(path[i])
		(xend, yend) = getMidPoint(path[i+1])
		can.create_line(xstart,ystart,xend,yend,fill='purple', width='4.0')


def draw_player(can, coord):
	(x,y) = getMidPoint(coord)	
	can.create_oval(x-10, y-10, x+10, y+10, fill='purple')
def draw_player2(can, coord):
        (x,y) = getMidPoint(coord)
        can.create_oval(x-10, y-10, x+10, y+10, fill='blue')

def draw_wall(can, wall):
	(x,y,direction) = wall
	if (direction == 'v'):
		xstart = 50*x +8*(x-1) + 2 
		ystart = 50*y + 8*y + 2
		width = 4 
		height = 103
	else:
		xstart = 50*x +8*x + 2 
		ystart = 50*y + 8*(y-1) + 2
		width = 103
		height = 4	
		
	can.create_rectangle(xstart,ystart, xstart+width, ystart+height, fill='brown')

def draw_mult_walls(can, wall_list):
	for w in wall_list:
		draw_wall(can, w)


def getMidPoint(coord):
	(x,y) = coord
	xtopleft = x*50+x*8
	ytopleft = y*50+y*8
	return (xtopleft+25, ytopleft+25)


if __name__ == '__main__':            
	window=Tk()
	canvas=Canvas(window,width=515,height=515)
	canvas.grid(row=0,column=0)
	canvas.update_idletasks() 






	# =====================================================================================
	# don't touch anything above this point	

	# once you have the board working, uncomment this line
	myboard = qu.QBoard()

	walls = [(1,0,'v'), (2,0,'v'), (0,2,'h'),  (6,2,'h'), (0,8,'h'), (2,8,'h'), (5,5,'v'), (1,4,'h'), (5,6,'h'), (5,3,'v'), (3,3,'v'), (3,4,'h')]
	
	# when you have the graph representation working, you can add the walls with the following loop 
	for w in walls:
		(x,y,d) = w
		myboard.addWall((x,y), d)

	# specify the destination here
	dest = (4,0)

	# specify start point here
	start = (4,8)


	# these lines should eventually draw the shortest path from start to dest
	myboard.placePlayer(start)
	draw_quoridor(canvas, myboard.getWalls(), myboard.shortestPathTo(dest),start)
        # ^ currently has another field that holds starting position of player 2
	# test call 
	#draw_quoridor(canvas, walls, [(4,8), (4,7), (4, 6)], start)
	window.mainloop()

	'''
	# to test, place walls in this list
	# Below here, read through the valid file and turn it into the game board

        '''
	
	f = raw_input("Enter a file containing quoridor moves.  The appropriate format is <turn number><color>.<column><row><OPTIONALdirection>\ni.e. 1b.e8 means on the first round black moves to the 8th position.\n")
	fp = open(f, 'r')
	for line in fp.readlines():
        #print line
        #f = raw_input("Enter a move in the format <turnnumber><color>.<col><row><walldirection>")
                move = line.split(";")
                for m in move:
                        m.rstrip() #strip whitespace
                        c,r = m[3],m[4] #tuple off the rows and columns
                        
        while f != "N":
                
                #b = parseMove(line);
                #i = 0 #turn counter -- %2 = 0 it must be player 1, %2 = 1 player 2
                #print b
                #for move in b:
                #move = move.rstrip()
            print(f)
            #gotta strip trailing whitespace or length won't work
            if len(f) != 6:
                #probably want to update the appropriate player
                if f[1] == 'w':
                        myboard.placePlayer((int(f[3]), int(f[4]))
                else:
                        myboard.placePlayer2((int(f[3]), int(f[4]))
                draw_quoridor(canvas, myboard.getWalls(), myboard.shortestPathTo(dest), myboard.getplayer, myboard.getplayer2)
                
                #gb.updateBoard(int(move[0]), move[1], -1, move[3:])
            else:
                # CHECK IF THE WALL TO SET IS VALID! E.G. add it, check if both sides can still win, and add it if so
                gb.updateBoard(int(move[0]), move[1], move[5], move[3:4])
                #ALTERNATIVELY, Take wall input, change into proper formatting
            gb.printBoard()   #print move[3:]
            i += 1
             
    #gb.updateBoard(1, "b", -1, "e8")
    #gb.printBoard()

'''
