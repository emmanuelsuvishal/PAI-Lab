from collections import deque

def bfs(capacity, start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        path = path + [state]

        # Goal check (4 liters in the first jug)
        if state[0] == goal:
            return path

        # Try all possible pours
        for i in range(3):
            for j in range(3):
                if i != j:
                    transfer = min(state[i], capacity[j] - state[j])
                    if transfer > 0:
                        new_state = list(state)
                        new_state[i] -= transfer
                        new_state[j] += transfer
                        queue.append((tuple(new_state), path))

    return None


# ------------------ MAIN ------------------

capacity = (8, 5, 3)
start = (8, 0, 0)
goal = 4

solution = bfs(capacity, start, goal)

print("BFS Solution Path:")
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found")
