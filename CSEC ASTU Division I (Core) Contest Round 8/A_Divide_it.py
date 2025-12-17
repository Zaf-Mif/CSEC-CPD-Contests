def solve(n):
    if n == 1:
        return 0
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        return -1
    cnt = 0
    while (n % 2 == 0 or n % 3 == 0 or n % 5 == 0) or n == 1:
        if n % 5 == 0:
            n = (4*n) // 5
            cnt += 1
        elif n % 3 == 0:
            n = (2 * n) // 3
            cnt += 1
        elif n % 2 == 0:
            n //= 2
            cnt += 1
        if n == 1:
            return cnt
    return -1
t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))