from collections import deque

def bfs(start, goal):
    q = deque([(start, [start])])
    visited = {start}

    while q:
        state, path = q.popleft()

        if state == goal:
            return path

        z = state.index(0)
        r, c = divmod(z, 3)

        moves = []
        if r > 0: moves.append(z - 3)
        if r < 2: moves.append(z + 3)
        if c > 0: moves.append(z - 1)
        if c < 2: moves.append(z + 1)

        for n in moves:
            x = list(state)
            x[z], x[n] = x[n], x[z]
            x = tuple(x)

            if x not in visited:
                visited.add(x)
                q.append((x, path + [x]))

start = (0, 1, 2,
         4, 5, 3,
         7, 8, 6)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

result = bfs(start, goal)

print("Solution found!")
print("Moves:", len(result) - 1)

for i, state in enumerate(result):
    print("\nStep", i)
    for j in range(0, 9, 3):
        print(state[j:j+3])
