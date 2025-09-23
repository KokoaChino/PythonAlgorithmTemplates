def kmp(s: str, t: str) -> int: # s：主串 t：目标串
    m, n = len(s), len(t)
    if n == 0:
        return -1
    next = [0 for _ in range(n)]
    j = 0
    for i in range(1, n):
        while j > 0 and t[i] != t[j]:
            j = next[j - 1]
        if t[i] == t[j]:
            j += 1
        next[i] = j
    j = 0
    for i in range(m):
        while j > 0 and s[i] != t[j]:
            j = next[j - 1]
        if s[i] == t[j]:
            j += 1
        if j == n:
            return i - n + 1
    return -1