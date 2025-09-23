def calc_z(s: str) -> list: # Z 函数
    n = len(s)
    z = [0] * n
    z[0] = n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = z[i - l] if z[i - l] < r - i + 1 else r - i + 1
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            l, r = i, i + z[i]
            z[i] += 1
    return z