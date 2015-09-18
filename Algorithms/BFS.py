#Will implement BFS here
def BFS(q,start):
	visited, queue = set(), [start]
	while queue:
		v = queue.pop(0)
		if not v in visited:
			visited.add(v)
			queue.extend(q[v] - visited)
	return visited	

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(BFS(graph, 'E'))

