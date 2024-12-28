import heapq

def a_star(graph, start, goal, heuristic):
    # Priority queue for nodes to explore
    open_list = []
    heapq.heappush(open_list, (0, start))  # (priority, node)

    # Keep track of costs
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    # Parent map for reconstructing the path
    came_from = {}

    while open_list:
        # Get the node with the lowest priority (f_score)
        current_f_score, current_node = heapq.heappop(open_list)

        # If we reached the goal, reconstruct and return the path
        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        for neighbor, weight in graph[current_node].items():
            # Calculate tentative g_score for neighbor
            tentative_g_score = g_score[current_node] + weight

            if tentative_g_score < g_score[neighbor]:
                # Update g_score and f_score
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]

                # Add neighbor to the open list
                heapq.heappush(open_list, (f_score, neighbor))

                # Record the path
                came_from[neighbor] = current_node

    return None  # No path found

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]  # Return reversed path

# Example graph as an adjacency list with weights
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'F': 2},
    'D': {'B': 1},
    'E': {'B': 4, 'F': 1},
    'F': {'C': 2, 'E': 1}
}

# Example heuristic (straight-line distance to the goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 1,
    'F': 0
}

# Finding the shortest path from 'A' to 'F'
start = 'A'
goal = 'F'
path = a_star(graph, start, goal, heuristic)

print("Shortest path:", path)
