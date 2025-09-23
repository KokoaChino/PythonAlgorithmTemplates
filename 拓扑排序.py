from collections import deque

def get(n: int, edges: list) -> list: # 返回该有向无环图的拓扑排序
    g, deg = [[] for _ in range(n)], [0] * n
    for u, v in edges:
        g[u].append(v)
        deg[v] += 1
    ans = [i for i in range(n) if deg[i] == 0]
    q = deque(ans)
    while q:
        for x in g[q.popleft()]:
            deg[x] -= 1
            if deg[x] == 0:
                q.append(x)
                ans.append(x)
    return ans if len(ans) == n else []