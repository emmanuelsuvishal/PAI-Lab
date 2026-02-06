def dfs(capacity, state, goal, visited, path):
    if state in visited:
        return None

    visited.add(state)
    path.append(state)

    # Goal: 4 liters in jug 1
    if state[0] == goal:
        return path

    for i in range(3):
        for j in range(3):
            if i != j:
                transfer = min(state[i], capacity[j] - state[j])
                if transfer > 0:
                    new_state = list(state)
                    new_state[i] -= transfer
                    new_state[j] += transfer

                    result = dfs(
                        capacity,
                        tuple(new_state),
                        goal,
                        visited,
                        path.copy()
                    )
                    if result:
                        return result

    return None


# ------------------ MAIN ------------------

capacity = (8, 5, 3)
start = (8, 0, 0)   # IMPORTANT
goal = 4

solution = dfs(capacity, start, goal, set(), [])

print("DFS Solution Path:")
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found")
