from heapq import heappush, heappop


# goal configuration stored as a tuple
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def misplaced_tiles(state):
    """Counts how many tiles are not in their correct goal position."""
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != GOAL[i])


def manhattan_distance(state):
    """Total Manhattan (grid) distance of tiles from their goal positions."""
    distance = 0
    for index, tile in enumerate(state):
        if tile == 0:
            continue  # skip blank tile
        goal_index = GOAL.index(tile)
        r1, c1 = divmod(index, 3)
        r2, c2 = divmod(goal_index, 3)
        distance += abs(r1 - r2) + abs(c1 - c2)
    return distance


def get_neighbors(state):
    """Returns all reachable states from the current state."""
    neighbors = []
    zero_pos = state.index(0)
    row, col = divmod(zero_pos, 3)
    # Moves allowed based on blank tile position
    possible_moves = []
    if row > 0:
        possible_moves.append(zero_pos - 3)  # Up
    if row < 2:
        possible_moves.append(zero_pos + 3)  # Down
    if col > 0:
        possible_moves.append(zero_pos - 1)  # Left
    if col < 2:
        possible_moves.append(zero_pos + 1)  # Right
    # Swap blank with its neighbor
    for move in possible_moves:
        lst = list(state)
        lst[zero_pos], lst[move] = lst[move], lst[zero_pos]
        neighbors.append(tuple(lst))
    return neighbors


def a_star(start, heuristic="manhattan"):
    """Runs A* using either Manhattan or Misplaced Tiles heuristic."""
    # Select the heuristic
    if heuristic == "manhattan":
        h = manhattan_distance
    elif heuristic == "misplaced":
        h = misplaced_tiles
    else:
        raise ValueError("Invalid heuristic name.")
    # Priority queue (f, g, state)
    open_list = []
    heappush(open_list, (h(start), 0, start))
    came_from = {}  # to reconstruct path
    g_cost = {start: 0}  # path cost
    visited = set()
    while open_list:
        _, cost, state = heappop(open_list)
        # Check if goal reached
        if state == GOAL:
            path = [state]
            while state in came_from:
                state = came_from[state]
                path.append(state)
            return path[::-1]
        visited.add(state)
        # Explore neighbors
        for next_state in get_neighbors(state):
            if next_state in visited:
                continue
            tentative_cost = g_cost[state] + 1  # every move costs 1
            if next_state not in g_cost or tentative_cost < g_cost[next_state]:
                came_from[next_state] = state
                g_cost[next_state] = tentative_cost
                f_score = tentative_cost + h(next_state)
                heappush(open_list, (f_score, tentative_cost, next_state))
    return None  # unsolvable


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


if __name__ == "__main__":
    start_state = (1, 2, 3,
                   0, 4, 6,
                   7, 5, 8)
    print("=== Solving using MISPLACED TILES heuristic ===")
    sol = a_star(start_state, heuristic="misplaced")
    if sol:
        print(f"Moves needed: {len(sol) - 1}")
        for step in sol:
            print_state(step)
    else:
        print("No solution found.")
    print("\n=== Solving using MANHATTAN heuristic ===")
    sol = a_star(start_state, heuristic="manhattan")
    if sol:
        print(f"Moves needed: {len(sol) - 1}")
        for step in sol:
            print_state(step)
    else:
        print("No solution found.")