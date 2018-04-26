from UGraph import UGraph


#to make compatible with drawing, need to 0 index starting with
# (0,0) in top left
'''     Original code written by Dr. Scott Yilek as part of pythonic implementation of Quoridor
        Any additions are noted below or inline and added/written by Elena Ryan

        Made some changes so that everything works with 2 players on the board.
        NOT elegant, but highly functional


'''

class QBoard:

	def __init__(self):
		self.graph = UGraph({})
		for i in range(0,9):
			for j in range(0,9):
				self.graph.addNode((i,j))
		for i in range(0,9):
			for j in range(0,9):
				self.graph.addEdge((i,j), (i,j-1),1)	 
				self.graph.addEdge((i,j), (i-1,j),1)	 
		self.walls = []
		self.player = (4,8)
		self.player2 = (4,0)
		self.winset = set([(i,0) for i in range(0,9)])


	def placePlayer(self, coord):
		self.player = coord
	def placePlayer2(self, coord):
                self.player2 = coord

	def addWall(self,topleftof, direction):
		(x,y) = topleftof
		self.walls.append((x,y,direction))
		if (direction == 'v'):
			# vertical wall
			self.graph.removeEdge((x,y), (x-1,y))			
			self.graph.removeEdge((x,y+1), (x-1,y+1))			
		elif (direction == 'h'):
			self.graph.removeEdge((x,y), (x,y-1))			
			self.graph.removeEdge((x+1,y), (x+1,y-1))			

	def getWalls(self):
		return self.walls

	#This is new and it's a little tough, but it will make it easier to create
	# valid, random games
	def setWalls(self, nwalls)
                self.walls = nwalls

	def canStillWin(self):
		reachable = self.graph.reachable_from(self.player)
		if (len(reachable.intersection(self.winset))==0):
			return False
		return True
	def canStillWin2(self):
		reachable = self.graph.reachable_from(self.player2)
		if (len(reachable.intersection(self.winset))==0):
			return False
		return True

	def getDistTo(self,coord):
		dist = {}
		self.graph.bfs(self.player, dist)
		if (coord in dist):
			return dist[coord]
		return None
	def getDistToP2(self,coord):
                dist = {}
                self.graph.bfs(self.player2, dist)
                if (coord in dist):
                        return dist[coord]
                return None

	def shortestPathTo(self,coord):
		dist = {}
		self.graph.bfs(self.player, dist)
		if (coord in dist):
			(lngth, prev) = dist[coord]
			path = [0]*(lngth+1)
			path[lngth] = coord 
			while (prev is not None):
				coord = prev		
				(lngth, prev) = dist[coord]
				path[lngth] = coord 
			return path

		return None
	def shortestPathToP2(self,coord):
                dist = {}
                self.graph.bfs(self.player2, dist)
                if (coord in dist):
                        (lngth, prev) = dist[coord]
                        path = [0]*(lngth+1)
                        path[lngth] = coord
                        while (prev is not None):
                                coord = prev
                                (lngth, prev) = dist[coord]
                                path[lngth] = coord
                        return path

                return None

	
        def getplayer(self):
                return self.player
        def getplayer2(self):
                return self.player2

	def __repr__(self):
		return str(self.graph)



