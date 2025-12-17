import heapq

def maxProbability(n, edges, succProb, start, end):
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for (u, v), p in zip(edges, succProb):
        graph[u].append((v, p))
        graph[v].append((u, p))

    # Distance array to store max probability to reach each node
    dist = [0.0] * n
    dist[start] = 1.0

    # Max heap (use negative values since Python has min-heap)
    heap = [(-1.0, start)]

    while heap:
        cur_prob, node = heapq.heappop(heap)
        cur_prob = -cur_prob  # convert back to positive

        # If we reached the end node, return the probability
        if node == end:
            return cur_prob

        # Traverse all neighbors
        for nei, prob in graph[node]:
            new_prob = cur_prob * prob
            if new_prob > dist[nei]:
                dist[nei] = new_prob
                heapq.heappush(heap, (-new_prob, nei))

    # If no path found
    return 0.0
