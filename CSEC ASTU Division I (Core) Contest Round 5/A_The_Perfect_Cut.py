def check(arr, n):
    l, r = 0, 0
    found = False
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            s1 = sum(arr[:i]) % 3
            s2 = sum(arr[i:j]) % 3
            s3 = sum(arr[j:]) % 3

            if (s1 == s2 == s3) or (len({s1, s2, s3}) == 3):
                l, r = i, j
                found = True
                break
        if found:
            return (l,r)
    return(0,0)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(*check(arr, n))