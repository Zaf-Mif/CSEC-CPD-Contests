def solve(r, c, grid):
    #  the wolf can move to neighbour cell which is up down left right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def is_safe():
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'W':
                    for dr, dc in directions:
                        ni, nj = i + dr, j + dc
                        if 0 <= ni < r and 0 <= nj < c:
                            if grid[ni][nj] == 'S':
                                return False
        return True
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                grid[i][j] = 'D'
    if is_safe():
        print("Yes")
        for row in grid:
            print(''.join(row))
    else:
        print ("No")

r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
solve(r, c, grid)