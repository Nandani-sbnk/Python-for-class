import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous

    def __lt__(self, other):
        return (self.moves + self.manhattan_distance()) < (other.moves + other.manhattan_distance())

    def find_blank_space(self):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == 0:
                    return i, j

    def manhattan_distance(self):
        """Calculate the Manhattan distance heuristic."""
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    target_x, target_y = divmod(self.
                                                board[i][j] - 1, 3)
                    distance += abs(target_x - i) + abs(target_y - j)
        return distance

    def is_goal(self):
        """Check if the current state is the goal state."""
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == goal

    def neighbors(self):
        """Generate neighboring states."""
        x, y = self.find_blank_space()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors

def solve_puzzle(initial_board):
    """Solve the 8-puzzle problem using A* search."""
    start_state = PuzzleState(initial_board)
    priority_queue = []
    heapq.heappush(priority_queue, start_state)
    visited = set()

    while priority_queue:
        current_state = heapq.heappop(priority_queue)

        if current_state.is_goal():
            return reconstruct_path(current_state)

        visited.add(tuple(map(tuple, current_state.board)))

        for neighbor in current_state.neighbors():
            if tuple(map(tuple, neighbor.board)) not in visited:
                heapq.heappush(priority_queue, neighbor)

    return None  # If no solution found

def reconstruct_path(state):
    """Reconstruct the path from the goal state to the initial state."""
    path = []
    while state:
        path.append(state.board)
        state = state.previous
    return path[::-1]

def print_board(board):
    for row in board:
        print(" ".join(str(x) if x != 0 else "_" for x in row))
    print()

# Example usage
if __name__ == "__main__":
    initial_board = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    solution = solve_puzzle(initial_board)
    if solution:
        print("Solution found:")
        for step, board in enumerate(solution):
            print(f"Step {step}:")
            print_board(board)
    else:
        print("No solution found.")
