def solve(n, x, y):
    # white move first then black
    # the king which reaches the (x,y) first wins
    # the king can move (a,b)to the cells (a+1,b), (a−1,b), (a,b+1), (a,b−1),
    #  (a+1,b−1), (a+1,b+1), (a−1,b−1), or (a−1,b+1) in any case we will have a winner 
    direction = {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)}
    # white = (1,1)
    # black = (n, n)
    # as a whit go first when both have the same distance white will win
    white = abs(x - 1) + abs(y - 1)
    black = abs(x - n) + abs(y - n)
    if white <= black:
        return "White"
    else:
        return "Black"
n = int(input())
x, y = map(int, input().split())
print(solve(n, x, y))