from collections import deque


class UGraph:
	# undirected graph will be adjacency list format
	# represented by a dictionary of dictionaries
	def __init__(self, d):
		self.adjlist = d
		self.genEdgeSet()

	def genEdgeSet(self):
		self.edges = set()
		for u in self.adjlist:
			for v in self.adjlist[u]:
				self.edges.add(frozenset([u,v])) 
	
	def addNode(self,label):
		self.adjlist[label] = {}

	def addEdge(self, u, v, wt):
		if (u in self.adjlist and v in self.adjlist):
			self.adjlist[u][v] = wt
			self.adjlist[v][u] = wt
			self.edges.add(frozenset([u,v]))

	def removeEdge(self, u, v):
		self.adjlist[u].pop(v, None)
		self.adjlist[v].pop(u, None)
		if (frozenset([u,v]) in self.edges):	
			self.edges.remove(frozenset([u,v]))

	def getEdgeWt(self, u, v):
		return self.adjlist[u][v]

	def getNeighbors(self, u):
		return self.adjlist[u].keys()

	def getEdgeSet(self):
		return self.edges

	def getNodeSet(self):
		return self.adjlist.keys()
	
	def __repr__(self):
		return str(self.adjlist)


	def drawDOT(self):
		thenodes = self.getNodeSet()
		i = 0
		nodes = {}
		for u in thenodes:
			nodes[str(u)]='a_'+str(i)
			i = i+1
		

		print "graph mygraph {"
		for n in nodes.keys():
			print nodes[n] + ' [label="' + n + '"]'


		for e in self.getEdgeSet(): 
			(u,v) = list(e)[0:2] 
			print nodes[str(u)] + ' -- ' + nodes[str(v)] + ' [label="' + str(self.getEdgeWt(u,v)) + '"]'
		print '}'





	def __getitem__(self, key):
		return self.adjlist[key]

	def reachable_from(self, u):
		# return set of nodes reachable from u.  Use dfs.
		S = set([u])
		self.dfs(u, S)
		return S 

	def dfs(self, u, visited):
		for v in self.getNeighbors(u):
			if (v not in visited):
				visited.add(v)
				self.dfs(v, visited)	

	def bfs(self, s, dist):
		dist[s] = (0, None)
		Q = deque([s])	
		while (len(Q)>0):
			u = Q.popleft()
			for v in self.getNeighbors(u):
				if (not v in dist):
					Q.append(v)
					dist[v] = (dist[u][0]+1, u)
		


