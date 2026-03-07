t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 1
    last = arr[0]
    for i in range(1, n):
        if arr[i] >= last + 2:
            cnt += 1
            last = arr[i]
    print(cnt)
