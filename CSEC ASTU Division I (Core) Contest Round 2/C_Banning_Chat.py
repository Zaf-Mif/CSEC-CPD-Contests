import math
def solve(k,x):
    if x >= k*k:
        return 2*k - 1

    asc = k*(k+1)//2
    if x <= asc:
        lo, hi, ans = 1, k, k
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid*(mid+1)//2 >= x:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
    else:
        y = x - asc
        lo, hi, p_ans = 1, k - 1, k - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid*k - mid*(mid+1)//2 >= y:
                p_ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return k + p_ans
t = int(input())
for _ in range(t):
    k, x = map(int,input().split())
    print(solve(k,x))
