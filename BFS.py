from collections import deque

def bfs(graph, start_node):
    # Create a queue for BFS and add the starting node
    queue = deque([start_node])
    # Keep track of visited nodes
    visited = set()
    visited.add(start_node)

    # BFS traversal
    while queue:
        # Dequeue a node from the queue
        current_node = queue.popleft()
        print(current_node, end=" ")  # Process the current node

        # Enqueue unvisited neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Starting BFS from node 'A'
print("BFS Traversal:")
bfs(graph, 'A')
