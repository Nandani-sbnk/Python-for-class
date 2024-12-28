def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the current node as visited
    visited.add(start_node)
    print(start_node, end=" ")  # Process the current node

    # Recursively visit unvisited neighbors
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Starting DFS from node 'A'
print("DFS Traversal:")
dfs(graph, 'A')
