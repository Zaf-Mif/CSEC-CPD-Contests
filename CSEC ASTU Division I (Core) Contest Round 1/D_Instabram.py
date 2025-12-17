def solve(n,k,a):
    #  we have to return Yes or No if yes print an array of s size k
    s = set(a)
    if len(s) < k:
        return 'No'
    
n, k = map(int,input().split())
a = list(map(int,input().split()))
print(solve(n,k,a))