graph = {'A':['B','D'],'B':['C'],'C':['E','F'],'D':[],'E':[],'F':[]}

def find_path(graph,start,end,path=[]):
	path = path + [start]
	if(start==end):
		return path
	if(not graph.has_key(start)):
		return None
	#shortestPath = None
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph,node,end,path)
			if newpath: return newpath
	return None

print(find_path(graph,'A','F'))

def find_shortest_path(graph,start,end,path=[]):
	path=path+[start]
	if(start==end):
		return path
	if(not graph.has_key(start)):
		return None
	shortestPath = None
	for node in graph[start]:
		if node not in path:
			newpath = find_shortest_path(graph,node,end,path)
			if newpath:
				if(not shortest or len(newpath) < len(path)):
					shortestPath = newpath
	return shortestPath

print(find_path(graph,'A','F'))