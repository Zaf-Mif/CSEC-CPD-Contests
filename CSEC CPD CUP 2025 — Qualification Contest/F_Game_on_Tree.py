n, t = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(n - 1):  
    u, v = map(int, input().split())
    edges[u - 1].append(v - 1)
    edges[v - 1].append(u - 1)
