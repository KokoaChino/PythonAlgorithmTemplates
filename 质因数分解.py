def get_primes(n: int) -> list: # 质因数分解
    i, ans = 2, []
    while i ** 2 <= n:
        if n % i == 0:
            ans.append([i, 0])
            while n % i == 0:
                n //= i
                ans[-1][1] += 1
        i += 1
    if n > 1:
        ans.append([n, 1])
    return ans