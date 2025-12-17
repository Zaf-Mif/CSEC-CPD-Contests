def solve(n,m, grid):
    # start from row 0 and spiral 
    # but we don't know where the spiral starts the spiral can start from any of the four corners + when it comes when it start we may face a problem like we have 543 in the corner and 1 when we finish the spiral we may not be able to connect them
    # in this case we can iterate over all four corners and for each corner we can do the spiral and count the number of 1543 the spiral can start from left right up down of the grid in any of the columns or rows
    # ite
    # we have to find how many 1543 are in result
    res = 0
    directions = [(0,1),(1,0),(0,-1),(-1,0)] # right down left up
    def count_1543(path):
        count = 0
        for i in range(len(path)-3):
            if path[i:i+4] == [1,5,4,3]:
                count += 1
        return count
    def spiral(r, c, dir_idx):
        visited = [[False]*m for _ in range(n)]
        path = []
        for _ in range(n*m):
            if 0 <= r < n and 0 <= c < m and not visited[r][c]:
                path.append(grid[r-1][c-1])
                visited[r][c] = True
            else:
                r -= directions[dir_idx][0]
                c -= directions[dir_idx][1]
                dir_idx = (dir_idx + 1) % 4
                r += directions[dir_idx][0]
                c += directions[dir_idx][1]
                path.append(grid[r][c])
                visited[r][c] = True
            r += directions[dir_idx][0]
            c += directions[dir_idx][1]
        return count_1543(path)
    max_count = 0
    for r in [0, n-1]:
        for start_col in [0, m-1]:
            for dir_idx in range(4):
                max_count = max(max_count, spiral(r, start_col, dir_idx))
    return max_count


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    print(solve(n, m, grid))