def solve(n, k, t):
    # max of the stand is k
    # minimum 0 if it is n + k and 0  

    b = n / k

    if t >= k and t <= (k*b):
        return k 
    if t < k :
        return(t)
    remain = k - (t % n)

    if t > b:
        return remain

n, k, t = map(int,input().split())
print(solve(n,k,t))

