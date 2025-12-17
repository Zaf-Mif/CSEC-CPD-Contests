def solve(n,a,m,b):
    # the pairs must differ by at most 1 this means they can be made equal
    cnt = 0
    a.sort()
    b.sort()    
    # by using two pointers we can count the number of pairs
    i = 0
    j = 0
    while i < n and j < m:
        if abs(a[i] - b[j]) <= 1:
            cnt += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return cnt
    
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
print(solve(n,a,m,b))