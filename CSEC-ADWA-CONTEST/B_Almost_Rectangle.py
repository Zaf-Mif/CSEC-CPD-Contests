t = int(input())

for _ in range(t):
    n = int(input())
    arr = []

    grid = []

    for i in range(n):
        row = list(input())
        grid.append(row)

        for j in range(n):
            if row[j] == "*":
                arr.append((i, j))

    (x1, y1), (x2, y2) = arr

    # case 1: same row
    if x1 == x2:
        nx = x1 + 1 if x1 + 1 < n else x1 - 1
        grid[nx][y1] = "*"
        grid[nx][y2] = "*"

    # case 2: same column
    elif y1 == y2:
        ny = y1 + 1 if y1 + 1 < n else y1 - 1
        grid[x1][ny] = "*"
        grid[x2][ny] = "*"

    # case 3: rectangle
    else:
        grid[x1][y2] = "*"
        grid[x2][y1] = "*"

    for row in grid:
        print("".join(row))