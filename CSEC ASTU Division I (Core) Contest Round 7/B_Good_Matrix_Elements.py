# main diagonal. whihch go from the top-left to the bottom-right.
# secondary diagonal. all iams which go from the top-right to the bottom-left.
# Elements of the "middle" row — the row which has exactly  rows above it and the same number of rows below it. whn row == n // 2 an column is form 0 to n
# Elements of the "middle" column — the column that has exactly  columns to the left of it and the same number of columns to the right of it. whn out column == n // 2 an row is form 0 to n

n = int(input())
mat = []
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
res = 0
# Main diagonal
for i in range(n):
    res += mat[i][i]
# Secondary diagonal
for i in range(n):
    res += mat[i][n - 1 - i]

mid = n // 2
# Middle row
for j in range(n):
    res += mat[mid][j]
# Middle column
for i in range(n):
    res += mat[i][mid]
# Remove the double counted middle element
res -= (3 * mat[mid][mid])
print(res)