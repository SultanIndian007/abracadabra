class Graph:
	def __init__(self, vertices):
		self.V = vertices 
		self.graph = []

	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	def printArr(self, dist):
		print("Vertex Distance from Source")
		for i in range(self.V):
			print("{0}\t\t{1}".format(i, dist[i]))
	
	def BellmanFord(self, src):
		dist = [float("Inf")] * self.V
		dist[src] = 0
		for _ in range(self.V - 1):
			for u, v, w in self.graph:
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
						dist[v] = dist[u] + w
		for u, v, w in self.graph:
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
						print("Graph contains negative weight cycle")
						return

		self.printArr(dist)

sizeG = int(input("Enter Size of Graph: "))
sizeE = int(input("Enter No. Of Edges: "))
g = Graph(sizeG)
while(sizeE!=0):
	edge_from, edge_to, cost = map(int,input().strip().split(" "))
	g.addEdge(edge_from, edge_to, cost)
	sizeE-=1
g.BellmanFord(0)
