from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

#--------------------------#
#	  this is our map      |
#--------------------------#
#			A              |
#		   / \             |
#		  B   C            |
#		 / \   \           | 
#		D   E	F          |
#--------------------------#

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

bfs(graph, 'A')