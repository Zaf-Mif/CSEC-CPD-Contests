def solution(n,s):
    check = False
    for i in range(1, n-1):
        if s[i] in (s[0:i] + s[i+1:]):
            check = True
            return 'Yes'
    return "No"

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solution(n,s))