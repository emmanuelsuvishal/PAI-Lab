import heapq

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Moves: Up, Down, Left, Right
moves = {'Up': -3, 'Down': 3, 'Left': -1, 'Right': 1}

# Precompute goal positions for efficiency
goal_pos_map = {tile: i for i, tile in enumerate(goal)}

# Check valid move
def valid_move(pos, move):
    if move == 'Left' and pos % 3 == 0:
        return False
    if move == 'Right' and pos % 3 == 2:
        return False
    if move == 'Up' and pos < 3:
        return False
    if move == 'Down' and pos > 5:
        return False
    return True

# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        goal_pos = goal_pos_map[tile]
        distance += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)
    return distance

# Generate new states
def get_neighbors(state):
    neighbors = []
    pos = state.index(0)
    for move, delta in moves.items():
        if valid_move(pos, move):
            new_pos = pos + delta
            new_state = list(state)
            new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]
            neighbors.append((tuple(new_state), move))
    return neighbors

# A* Search
def a_star(start):
    open_list = []
    heapq.heappush(open_list, (heuristic(start), 0, start, []))  # f, g, state, path
    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)
        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path  # return list of moves

        for neighbor, move in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(open_list, (g + 1 + heuristic(neighbor), g + 1, neighbor, path + [move]))
    return None

# Function to print puzzle in 3x3 format
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Example usage
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solution_moves = a_star(start)

if solution_moves:
    print("Solution Moves:")
    print(solution_moves)
    
    # Show states step by step
    current_state = start
    print("\nPuzzle Steps:")
    print_puzzle(current_state)
    for move in solution_moves:
        pos = current_state.index(0)
        delta = moves[move]
        new_pos = pos + delta
        state_list = list(current_state)
        state_list[pos], state_list[new_pos] = state_list[new_pos], state_list[pos]
        current_state = tuple(state_list)
        print(f"Move: {move}")
        print_puzzle(current_state)
else:
    print("No solution found!")

