def get_inv(n: int, MOD = 10 ** 9 + 7) -> list: # 返回所有位于 [1, n] 的整数在模 MOD 意义下的乘法逆元
    inv = [1] * (n + 1)
    for i in range(2, n + 1):
        inv[i] = (MOD - MOD // i) * inv[MOD % i] % MOD
    return inv