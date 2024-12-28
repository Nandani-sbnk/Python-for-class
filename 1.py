from collections import deque

def bfs (graph,startnode):
    queue=deque([startnode])

    visited=set()

    visited.add(startnode)

    while queue:

        currentnode=queue.popleft()

        print(currentnode,end=" ")

        for neighbor in graph[currentnode]:
            if neighbor not in  visited:
              visited.add(neighbor)
              queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}             
bfs(graph,'A')