from heapq import heappush, heappop
from math import inf
from collections import deque

def dijkstra(mat: list, a: int) -> list: # 单源最短路
    n = len(mat)
    ans = [inf] * n
    ans[a] = 0
    q = deque([a])
    while q:
        x = q.popleft()
        for y, d in enumerate(mat[x]):
            if ans[y] > ans[x] + d:
                ans[y] = ans[x] + d
                q.append(y)
    return ans

def dijkstra(g: list, a: int) -> list: # 堆优化的单源最短路
    n = len(g)
    ans, st, q = [inf] * n, [False] * n, []
    ans[a] = 0
    heappush(q, (0, a))
    while q:
        dist, x = heappop(q)
        if st[x]:
            continue
        st[x] = True
        for t in g[x]:
            y, d = t
            if ans[y] > ans[x] + d:
                ans[y] = ans[x] + d
                heappush(q, (ans[y], y))
    return ans