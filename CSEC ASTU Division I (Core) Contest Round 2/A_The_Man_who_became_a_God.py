def solve(n,k,arr):
    #  we must split n len of arr into k parts 
    # f(l,r) = |al−al+1|+|al+1−al+2|+…+|ar−1−ar|
    # time complexity can pass  n,k (1≤k≤n≤100)
    dif = []
    for i in range(1,n):
        dif.append(abs(arr[i] - arr[i-1]))
    
    dif.sort(reverse = True)
    return sum(dif[k-1:])
    

t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solve(n,k,arr))
