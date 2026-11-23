import random


def compute_conflicts(state):
    """Returns the number of attacking queen pairs."""
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            same_col = state[i] == state[j]
            same_diag = abs(state[i] - state[j]) == abs(i - j)
            if same_col or same_diag:
                attacks += 1
    return attacks


def random_board(n):
    """Random placement of n queens (1 per row)."""
    return [random.randrange(n) for _ in range(n)]


def generate_neighbors(state):
    """Returns all boards where one queen moves to a different column."""
    neighbors = []
    n = len(state)
    for row in range(n):
        for col in range(n):
            if col != state[row]:
                new_state = state.copy()
                new_state[row] = col
                neighbors.append(new_state)
    return neighbors


def hill_climb(n):
    current = random_board(n)
    current_cost = compute_conflicts(current)
    step = 0
    print(f"Initial Board: {current} | Conflicts = {current_cost}\n")
    while True:
        neighbors = generate_neighbors(current)
        scores = [compute_conflicts(nb) for nb in neighbors]
        lowest = min(scores)
        # Select all equally good neighbors and pick one randomly
        candidates = [
            neighbors[i] for i in range(len(neighbors)) if scores[i] == lowest
        ]
        chosen = random.choice(candidates)
        print(f"Step {step}:")
        print(f" Current: {current} | Cost = {current_cost}")
        print(f" Best Move: {chosen} | New Cost = {lowest}\n")
        step += 1
        # No improvement → local optimum reached
        if lowest >= current_cost:
            print("Algorithm stopped: Local optimum reached.\n")
            return current, current_cost
        current, current_cost = chosen, lowest


solution, final_cost = hill_climb(4)
print("Final Solution Found:")
print(f"State: {solution}")
print(f"Heuristic Cost: {final_cost}\n")


def print_board(state):
    n = len(state)
    for r in range(n):
        row_str = ""
        for c in range(n):
            row_str += "Q " if state[r] == c else ". "
        print(row_str)
    print()


print("Final Board Layout:")
print_board(solution)