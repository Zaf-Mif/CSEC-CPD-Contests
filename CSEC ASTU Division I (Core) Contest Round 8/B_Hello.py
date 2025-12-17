def solve(s):
    # hello
    hell0 = ['h', 'e', 'l', 'l', 'o']
    idx = 0
    for i in range(len(s)):
        if idx < 5 and s[i] == hell0[idx]:
            idx += 1
    if idx == 5:
        return ("YES")
    else:
        return ("NO")
    
s = input()
print(solve(s))