def dls(s, g, limit, path):
    if s == g:
        return path
    if limit == 0:
        return None

    z = s.index(0)
    r, c = divmod(z, 3)

    moves = []
    if r > 0: moves.append(z - 3)
    if r < 2: moves.append(z + 3)
    if c > 0: moves.append(z - 1)
    if c < 2: moves.append(z + 1)

    for nz in moves:
        x = list(s)
        x[z], x[nz] = x[nz], x[z]
        x = tuple(x)

        if x not in path:
            res = dls(x, g, limit - 1, path + [x])
            if res:
                return res


def iddfs(start, goal):
    depth = 0
    while True:
        result = dls(start, goal, depth, [start])
        if result:
            return result
        depth += 1


start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

result = iddfs(start, goal)

print("Moves:", len(result) - 1)

for s in result:
    print(s[:3])
    print(s[3:6])
    print(s[6:])
    print()
