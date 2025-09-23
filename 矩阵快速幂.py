from copy import deepcopy

def mat_mul(a: list, b: list, MOD = 10 ** 9 + 7) -> list: # 矩阵乘法 a * b = c
    m, t, n = len(a), len(b), len(b[0])
    c = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            c[i][j] = sum(a[i][k] * b[k][j] for k in range(t)) % MOD
    return c

def mat_pow(a: list, n: int) -> list: # 矩阵幂运算 a ^ n = res
    m = len(a)
    res, a = [[0] * m for _ in range(m)], deepcopy(a)
    for i in range(m):
        res[i][i] = 1
    while n:
        if n & 1:
            res = mat_mul(res, a)
        n >>= 1
        a = mat_mul(a, a)
    return res



import numpy as np

def mat_pow(a: list, n: int, MOD = 10 ** 9 + 7) -> list: # 矩阵幂运算 a ^ n = res
    a = np.array(a, dtype=object)
    res = np.eye(a.shape[0], dtype=object)
    while n:
        if n & 1:
            res = np.dot(res, a) % MOD
        n >>= 1
        a = np.dot(a, a) % MOD
    return res.tolist()
