def get_isP(s: str) -> list: # 判断子串 s[i:j] 是否是回文的
    n = len(s)
    ans = [[True] * n for _ in range(n)]
    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            ans[i][j] = s[i] == s[j] and ans[i + 1][j - 1]
    return ans