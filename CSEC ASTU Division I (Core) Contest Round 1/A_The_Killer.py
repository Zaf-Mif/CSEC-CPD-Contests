n, m, z = map(int,input().split())
narr , marr = [], []
for i in range (n, z+1, n):
    narr.append(i)
for i in range (m, z+1, m):
    marr.append(i)
# print(narr, marr)
cnt = 0
nar = set(narr)
marr = set(marr)
for i in narr:
    if i in marr:
        cnt += 1
print(cnt)
