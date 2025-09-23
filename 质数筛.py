def get_primes(n: int) -> list: # 埃氏筛
    if n < 2:
        return [False] * (n + 1)
    ans = [True] * (n + 1)
    ans[0] = ans[1] = False
    for i in range(2, n + 1):
        if ans[i]:
            for j in range(i * i, n + 1, i):
                ans[j] = False
    return ans