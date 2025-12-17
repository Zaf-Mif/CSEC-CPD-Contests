def solve (n, party):
    alice = party[0]
    total = sum(party)
    #  alice must have strictly more than half
    ans = [1]
    coseat = alice
    for i in range(1, n):
        if party[i] * 2 <= alice:
            ans.append(i + 1)
            coseat += party[i]
    if coseat > total / 2:
        result = [str(len(ans))]
        result.append(' '.join(map(str, ans)))
        return '\n'.join(result)
    else:
        return '0' 

n = int(input())
party = list(map(int,input().split()))
print(solve(n, party))
